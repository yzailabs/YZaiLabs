import random
import time
from skills.skill import (
    post_action,
    get_portfolio,
    get_proposals,
    vote_proposal,
    proposal_forum_post,
    proposal_whitelist,
    proposal_forum_get,
    get_presales,
    project_forum_get,
    project_forum_post,
    get_presale_participants,
    presale_buy,
    get_presale_distribution_progress,
    presale_claim
)
from ai.proposal_analyzer import analyze_proposal
from ai.presale_analyzer import analyze_presale
import asyncio
import json


DUMMY_ACTIONS = [
    "looking around",
    "checking the market",
    "watching liquidity",
    "something feels interesting",
    "monitoring activity",
    "observing the chain",
    "tracking movements",
    "checking signals",
    "watching the memecoins",
    "searching for alpha"
]


def run_logic(agent):

    agent_id = agent["agent_id"]
    name = agent["name"]
    trading_style = agent["trading_style"]
    agent_wallet = agent["wallet_address"]

    print(f"[{name}] logic started")

    while True:

        try:

            # GET PORTFOLIO
            portfolio = get_portfolio(agent_id)

            total_value = portfolio["total_value"]
            pnl = portfolio["total_pnl"]
            bnb_balance = float(portfolio["bnb_balance"])

            print(f"[{name}] portfolio value: ${total_value} | pnl: {pnl} | bnb: {bnb_balance}")

            # action = random.choice(DUMMY_ACTIONS)
            # post_action(agent_id, action)
            # print(f"[{name}] {action}")

            # GET PROPOSALS
            proposals = get_proposals(order="desc")

            if not proposals:
                print(f"[{name}] no proposals found")

            else:

                for proposal in proposals:

                    proposal_id = proposal["id"]
                    proposal_name = proposal["name"]

                    print(f"[{name}] analyze proposal: {proposal_name}")

                    ai_result = asyncio.run(analyze_proposal(agent, proposal))

                    try:
                        decision = json.loads(ai_result)
                    except:
                        print(f"[{name}] AI returned invalid response")
                        decision = {"decision": "ignore"}

                    if decision["decision"] == "vote":

                        try:
                            vote_proposal(agent_id, proposal_id, True)
                            print(f"[{name}] voted for proposal {proposal_name}")
                        except Exception as e:
                            print(f"[{name}] vote error:", e)

                        try:

                            forum_data = proposal_forum_get(proposal_id)

                            already_posted = False

                            if forum_data:

                                for post in forum_data:

                                    if post.get("agent_id") == agent_id:
                                        already_posted = True
                                        break

                            if already_posted:

                                print(f"[{name}] already posted in forum")

                            else:

                                message = decision.get(
                                    "forum_message",
                                    "Interesting proposal."
                                )

                                proposal_forum_post(agent_id, proposal_id, message)

                                print(f"[{name}] posted forum message")

                        except Exception as e:

                            print(f"[{name}] forum error:", e)

                        if decision.get("whitelist"):

                            try:
                                proposal_whitelist(agent_id, agent_wallet, proposal_id, True)

                                print(f"[{name}] requested whitelist")

                            except Exception as e:

                                print(f"[{name}] whitelist error:", e)
                    else:
                        print(f"[{name}] AI ignored proposal {proposal_name}")

            # =====================
            # PRESALE LOGIC
            # =====================

            presales = get_presales()

            if presales["total"] == 0:
                print(f"[{name}] no presales found")

            else:

                for sale in presales["sales"]:

                    project = sale["proposal"]
                    project_id = project["id"]
                    project_name = project["name"]
                    token = sale["token_address"]
                    sale_contract = sale["sale_proxy_contract"]
                    min_buy = float(sale["min_buy_bnb"])
                    max_buy = float(sale["max_buy_bnb"])
                    status = sale["status"]

                    print(f"[{name}] analyze presale: {project_name}")

                    # =====================
                    # check forum
                    # =====================

                    forum = project_forum_get(project_id)

                    posted = False

                    for post in forum:
                        if post["agent_id"] == agent_id:
                            posted = True
                            break


                    # =====================
                    # AI analyze presale
                    # =====================

                    ai_result = asyncio.run(
                        analyze_presale(agent, sale, float(bnb_balance))
                    )

                    try:
                        decision = json.loads(ai_result)
                    except:
                        print(f"[{name}] invalid AI response")
                        continue

                    # =====================
                    # forum post
                    # =====================

                    if not posted:

                        try:
                            project_forum_post(
                                agent_id,
                                project_id,
                                decision.get("forum_message", "Interesting presale.")
                            )

                            print(f"[{name}] posted presale forum")

                        except Exception as e:
                            print(f"[{name}] presale forum error:", e)

                    # =====================
                    # check participation
                    # =====================

                    participants = get_presale_participants(token)

                    joined = False

                    for p in participants["participants"]:
                        if p["address"].lower() == agent_wallet.lower():
                            joined = True
                            break

                    if joined:
                        print(f"[{name}] already joined presale {project_name}")
                        continue

                    # =====================
                    # participate
                    # =====================

                    status = sale["status"]

                    # =====================
                    # UPCOMING SALE
                    # =====================

                    if status == "upcoming":
                        print(f"[{name}] presale {project_name} not started yet")
                        continue

                    # =====================
                    # LIVE SALE
                    # =====================

                    if status == "live" and decision.get("participate"):

                        amount = decision.get("amount_bnb", 0)
                        gas_reserve = 0.05
                        available = max(bnb_balance - gas_reserve, 0)

                        if amount > available:
                            amount = available * 0.9
                        print(
                            f"[{name}] try buy presale {project_name} with {amount} BNB"
                        )

                        try:

                            if amount < min_buy:
                                print(f"[{name}] amount below presale minimum, skipping")
                                continue

                            presale_buy(
                                agent_id,
                                sale_contract,
                                amount
                            )

                            print(
                                f"[{name}] joined presale {project_name} with {amount} BNB"
                            )

                        except Exception as e:
                            print(f"[{name}] presale buy error:", e)

                    # =====================
                    # ENDED SALE
                    # =====================

                    if status == "ended":
                        if status == "ended":
                            try:
                                progress = get_presale_distribution_progress(token)
                                dist_status = progress["status"]

                                if dist_status == "distributing":
                                    print(f"[{name}] claim tokens from {project_name}")
                                    presale_claim(agent_id, token)

                                elif dist_status == "completed":
                                    print(f"[{name}] distribution finished for {project_name}")

                            except Exception as e:
                                print(f"[{name}] distribution check error:", e)

        except Exception as e:

            print(f"[{name}] logic error:", e)

        time.sleep(random.randint(25, 45))