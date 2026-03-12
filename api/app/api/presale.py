from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import AsyncSessionLocal
from app.models.presale import Presale
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.proposal import Proposal
from app.core.onchain import (
    build_sale_params,
    is_agent_approved,
    approve_agent,
    create_sale,
    add_to_whitelist,
    get_participants,
    get_participant_count,
    emergency_cancel,
    claim_tokens,
    get_refund,
    finalize_sale_and_distribute,
    remove_from_whitelist,
)
from app.core.wallet_crypto import decrypt_private_key
from app.models.agent import Agent
from app.core.onchain import wait_and_extract_sale, get_sale_info
import os
from fastapi import Header
from typing import Optional, List
from app.models.agent_action import AgentAction
from app.core.onchain import get_all_sales
from datetime import datetime, timezone

INTERNAL_API_KEY = os.getenv("YZAI_INTERNAL_API_KEY")

router = APIRouter()

async def verify_internal_api_key(x_yzai_key: str = Header(None)):
    if not x_yzai_key or x_yzai_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


class PresaleCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    min_buy_bnb: float
    max_buy_bnb: float
    enable_whitelist: bool
    proposal_id: str

class WhitelistRequest(BaseModel):
    proposal_id: str
    addresses: List[str]

class EmergencyCancelRequest(BaseModel):
    agent_id: str
    token_address: str

class ClaimRequest(BaseModel):
    agent_id: str
    token_address: str


class RefundRequest(BaseModel):
    agent_id: str
    token_address: str


class FinalizeRequest(BaseModel):
    proposal_id: str
    token_address: str
    limit: int = 100


class RemoveWhitelistRequest(BaseModel):
    proposal_id: str
    token_address: str
    users: List[str]

@router.post("/")
async def create_presale(
    data: PresaleCreate,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_internal_api_key)
):

    if data.end_time <= data.start_time:
        raise HTTPException(status_code=400, detail="End time must be after start time")

    # Load Proposal
    result = await db.execute(
        select(Proposal).where(Proposal.id == data.proposal_id)
    )
    proposal = result.scalar_one_or_none()

    if not proposal:
        raise HTTPException(status_code=404, detail="Proposal not found")

    # Load Agent
    agent_result = await db.execute(
        select(Agent).where(Agent.id == proposal.owner)
    )
    agent = agent_result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    # Approve Agent if needed
    if not is_agent_approved(agent.wallet_address):
        approve_agent(agent.wallet_address)

    # Decrypt agent private key
    agent_pk = decrypt_private_key(agent.private_key_encrypted)

    sale_params, predicted_token = build_sale_params(proposal, data)

    tx_hash = create_sale(agent_pk, sale_params, value_eth=0.1)

    emitted_token, sale_proxy = wait_and_extract_sale(tx_hash)

    if emitted_token.lower() != predicted_token.lower():
        raise Exception("CREATE2 mismatch")

    token_address = predicted_token

    from app.core.onchain import get_sale_proxy_from_tx

    sale_proxy_contract = get_sale_proxy_from_tx(tx_hash)

    # Save Presale record
    presale = Presale(
        start_time=data.start_time,
        end_time=data.end_time,
        min_buy_bnb=data.min_buy_bnb,
        max_buy_bnb=data.max_buy_bnb,
        proposal_id=data.proposal_id,
        token_address=token_address,
        sale_proxy_contract=sale_proxy_contract
    )

    db.add(presale)
    await db.commit()
    await db.refresh(presale)

    # Log to AgentAction
    action_text = (
        f"Created presale for {proposal.name} ({proposal.ticker}) "
    )

    action = AgentAction(
        agent_id=agent.id,
        agent_name=agent.name,
        agent_address=agent.wallet_address,
        action=action_text
    )

    db.add(action)
    await db.commit()

    return {
        "presale_id": str(presale.id),
        "tx_hash": tx_hash
    }

@router.get("/")
async def get_presales(
    proposal_id: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):

    query = select(Presale)

    if proposal_id:
        query = query.where(Presale.proposal_id == proposal_id)

    result = await db.execute(query)
    presales = result.scalars().all()

    return [
        {
            "id": str(p.id),
            "proposal_id": str(p.proposal_id),
            "start_time": p.start_time,
            "end_time": p.end_time,
            "min_buy_bnb": p.min_buy_bnb,
            "max_buy_bnb": p.max_buy_bnb,
            "token_address": p.token_address,
            "sale_proxy_contract": p.sale_proxy_contract
        }
        for p in presales
    ]

@router.post("/sync/{token_address}")
async def sync_sale(token_address: str, db: AsyncSession = Depends(get_db)):

    from app.core.onchain import get_sale_info

    sale_info = get_sale_info(token_address)

    result = await db.execute(
        select(Presale).where(Presale.token_address == token_address)
    )

    presale = result.scalar_one_or_none()

    if not presale:
        raise HTTPException(status_code=404, detail="Presale not found")

    # Example: update times from onchain
    params = sale_info[4]

    presale.start_time = datetime.fromtimestamp(params[1])
    presale.end_time = datetime.fromtimestamp(params[2])

    await db.commit()

    return {"status": "synced"}

@router.post("/whitelist/{token_address}")
async def whitelist_users(
    token_address: str,
    data: WhitelistRequest,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_internal_api_key)
):

    # =========================
    # Load Proposal
    # =========================
    result = await db.execute(
        select(Proposal).where(Proposal.id == data.proposal_id)
    )
    proposal = result.scalar_one_or_none()

    if not proposal:
        raise HTTPException(status_code=404, detail="Proposal not found")

    # =========================
    # Load Agent
    # =========================
    agent_result = await db.execute(
        select(Agent).where(Agent.id == proposal.owner)
    )
    agent = agent_result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    # =========================
    # Approve Agent if needed
    # =========================
    if not is_agent_approved(agent.wallet_address):
        approve_agent(agent.wallet_address)

    # =========================
    # Decrypt Agent PK
    # =========================
    agent_pk = decrypt_private_key(agent.private_key_encrypted)

    # =========================
    # Send Whitelist TX (Agent Wallet)
    # =========================
    tx_hash = add_to_whitelist(
        agent_pk,
        token_address,
        data.addresses
    )

    return {
        "status": "submitted",
        "tx_hash": tx_hash
    }

@router.get("/participants/{token_address}")
async def participants(
    token_address: str,
    offset: int = 0,
    limit: int = 50
):

    data = get_participants(token_address, offset, limit)

    return {
        "token": token_address,
        "offset": offset,
        "limit": limit,
        "total": data["total"],
        "participants": [
            {
                "address": addr,
                "amount": data["amounts"][i]
            }
            for i, addr in enumerate(data["participants"])
        ]
    }

@router.get("/participants/{token_address}/count")
async def participant_count(token_address: str):

    count = get_participant_count(token_address)

    return {
        "token": token_address,
        "count": count
    }

@router.get("/sales")
async def get_all_sales_endpoint():

    sales = get_all_sales()

    return {
        "total": len(sales),
        "sales": sales
    }

@router.get("/sales/info")
async def get_sales_info(
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Presale, Proposal)
        .join(Proposal, Presale.proposal_id == Proposal.id)
    )

    rows = result.all()

    sales = []
    now = datetime.now(timezone.utc)

    for presale, proposal in rows:

        if presale.start_time > now:
            sale_status = "upcoming"
        elif presale.start_time <= now <= presale.end_time:
            sale_status = "live"
        else:
            sale_status = "ended"

        if status and sale_status != status:
            continue

        sales.append({
            "presale_id": str(presale.id),

            "token_address": presale.token_address,
            "sale_proxy_contract": presale.sale_proxy_contract,

            "start_time": presale.start_time,
            "end_time": presale.end_time,

            "min_buy_bnb": presale.min_buy_bnb,
            "max_buy_bnb": presale.max_buy_bnb,

            "status": sale_status,

            "proposal": {
                "id": str(proposal.id),
                "name": proposal.name,
                "ticker": proposal.ticker,
                "logo": proposal.logo,
                "description": proposal.description,
                "raise_amount": proposal.raise_amount,

                "website": proposal.website,
                "telegram": proposal.telegram,
                "twitter": proposal.twitter,
                "discord": proposal.discord
            },

            "tax_allocation": {
                "beneficiary_address": proposal.beneficiary_address,
                "buyback": proposal.buyback,
                "burn": proposal.burn,
                "treasury": proposal.treasury,
                "liquidity": proposal.liquidity
            }
        })

    return {
        "total": len(sales),
        "filter": status,
        "sales": sales
    }

@router.post("/emergency-cancel")
async def emergency_cancel_presale(
    data: EmergencyCancelRequest,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_internal_api_key)
):

    # =========================
    # Load Agent
    # =========================
    result = await db.execute(
        select(Agent).where(Agent.id == data.agent_id)
    )

    agent = result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    # =========================
    # Decrypt agent private key
    # =========================
    agent_pk = decrypt_private_key(agent.private_key_encrypted)

    # =========================
    # Send emergencyCancel tx
    # =========================
    tx_hash = emergency_cancel(
        agent_pk,
        data.token_address
    )

    # =========================
    # Log action
    # =========================
    action = AgentAction(
        agent_id=agent.id,
        agent_name=agent.name,
        agent_address=agent.wallet_address,
        action=f"Emergency cancelled presale for {data.token_address}"
    )

    db.add(action)
    await db.commit()

    return {
        "status": "submitted",
        "agent_id": str(agent.id),
        "token_address": data.token_address,
        "tx_hash": tx_hash
    }

@router.post("/claim")
async def claim_presale_tokens(
    data: ClaimRequest,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_internal_api_key)
):

    result = await db.execute(
        select(Agent).where(Agent.id == data.agent_id)
    )
    agent = result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent_pk = decrypt_private_key(agent.private_key_encrypted)

    tx_hash = claim_tokens(
        agent_pk,
        data.token_address
    )

    return {
        "status": "submitted",
        "tx_hash": tx_hash
    }

@router.post("/refund")
async def refund_presale(
    data: RefundRequest,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_internal_api_key)
):

    result = await db.execute(
        select(Agent).where(Agent.id == data.agent_id)
    )
    agent = result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent_pk = decrypt_private_key(agent.private_key_encrypted)

    tx_hash = get_refund(
        agent_pk,
        data.token_address
    )

    return {
        "status": "submitted",
        "tx_hash": tx_hash
    }

@router.post("/finalize")
async def finalize_presale(
    data: FinalizeRequest,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_internal_api_key)
):

    result = await db.execute(
        select(Proposal).where(Proposal.id == data.proposal_id)
    )
    proposal = result.scalar_one_or_none()

    if not proposal:
        raise HTTPException(status_code=404, detail="Proposal not found")

    agent_result = await db.execute(
        select(Agent).where(Agent.id == proposal.owner)
    )
    agent = agent_result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent_pk = decrypt_private_key(agent.private_key_encrypted)

    tx_hash = finalize_sale_and_distribute(
        agent_pk,
        data.token_address,
        data.limit
    )

    return {
        "status": "submitted",
        "tx_hash": tx_hash
    }

@router.post("/remove-whitelist")
async def remove_whitelist(
    data: RemoveWhitelistRequest,
    db: AsyncSession = Depends(get_db),
    _: None = Depends(verify_internal_api_key)
):

    result = await db.execute(
        select(Proposal).where(Proposal.id == data.proposal_id)
    )
    proposal = result.scalar_one_or_none()

    if not proposal:
        raise HTTPException(status_code=404, detail="Proposal not found")

    agent_result = await db.execute(
        select(Agent).where(Agent.id == proposal.owner)
    )
    agent = agent_result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent_pk = decrypt_private_key(agent.private_key_encrypted)

    tx_hash = remove_from_whitelist(
        agent_pk,
        data.token_address,
        data.users
    )

    return {
        "status": "submitted",
        "tx_hash": tx_hash
    }