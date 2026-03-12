from ai.client import generate_response
from ai.prompt_builder import TRADING_STYLE_RULES
from ai.prompt_builder import STYLE_PERSONALITY

async def analyze_presale(agent, presale, bnb_balance):

    proposal = presale["proposal"]

    name = proposal.get("name")
    description = proposal.get("description")
    website = proposal.get("website")
    twitter = proposal.get("twitter")

    min_buy = float(presale["min_buy_bnb"])
    max_buy = float(presale["max_buy_bnb"])
    bnb_balance = float(bnb_balance)

    trading_style = agent["trading_style"].lower()
    style_personality = STYLE_PERSONALITY.get(trading_style, "")
    trading_rules = TRADING_STYLE_RULES.get(trading_style, "")

    gas_reserve = 0.05

    available_bnb = max(bnb_balance - gas_reserve, 0)

    STYLE_MAX_ALLOCATION = {
        "conservative": 0.15,
        "steady": 0.30,
        "aggressive": 0.70,
        "diamond": 0.50
    }

    max_alloc = STYLE_MAX_ALLOCATION.get(trading_style, 0.30)

    max_position = available_bnb * max_alloc
    max_allowed = min(max_position, max_buy)
    max_allowed = round(max_allowed, 4)
    if max_allowed < min_buy:
        return '{"participate": false, "amount_bnb": 0, "forum_message": "Minimum buy is larger than my current allocation limit. Sitting this one out."}'

    system_prompt = f"""
You are an autonomous AI venture capital agent.

Trading Style: {trading_style}

Rules:
{trading_rules}

Important constraints:

Wallet balance: {bnb_balance}
Gas reserve: 0.05 BNB
Available capital: {available_bnb}

Maximum allowed position by style: {max_alloc*100}%

Maximum allowed presale buy: {max_allowed} BNB

Forum personality:

{style_personality}

Forum message rules:

- 2 to 4 sentences
- Mention something specific from the project
- Explain briefly why it is interesting or risky
- Natural conversational tone
- Slightly witty or humorous
- Smart humor (dry / subtle), not memes
- Not corporate
- Not childish

Return STRICT JSON:

{{
"participate": true | false,
"amount_bnb": number,
"forum_message": "2-4 sentence opinion about the project"
}}

Rules:

- Must be >= {min_buy}
- Must be <= {max_allowed}
- Always respect presale minimum buy.
- Never suggest amount below min_buy.
- NEVER use entire wallet
- Always leave gas reserve
"""

    user_prompt = f"""
Project: {name}

Website:
{website}

Twitter:
{twitter}

Description:
{description}

Presale limits:
min buy: {min_buy}
max buy: {max_buy}

Wallet BNB balance:
{bnb_balance}
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return await generate_response(messages)