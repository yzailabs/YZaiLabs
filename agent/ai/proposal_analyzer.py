from ai.client import generate_response
from ai.prompt_builder import build_proposal_prompt
# from ai.prompt_builder import TRADING_STYLE_RULES

TRADING_STYLE_RULES = {
    "conservative": """
Maximum position size per asset: 15%
One-time purchase of 15%
Take profit at +100% sell 30%
Stop loss at -50%
""",
    "steady": """
Max position 30%
Build in 3 batches 10% + 10% + 10%
Stop loss -50%
""",
    "aggressive": """
Max position 70%
2 batches 15% + 15%
Stop loss -50%
""",
    "diamond": """
Max position 50%
No take-profit
Stop loss -50%
"""
}

async def analyze_proposal(agent, proposal):

    name = proposal["name"]
    description = proposal.get("description", "")
    website = proposal.get("website", "")
    twitter = proposal.get("twitter", "")
    raise_amount = proposal.get("raise_amount", 0)

    trading_style = agent["trading_style"].lower()
    trading_rules = TRADING_STYLE_RULES.get(trading_style, "")

    human_message = f"""
You are evaluating a startup proposal as an AI venture capital agent.

Proposal:
Name: {name}
Raise Amount: {raise_amount}

Website:
{website}

Twitter:
{twitter}

Description:
{description}

Your trading style is: {trading_style}

Trading rules you must follow:
{trading_rules}

Decision guidelines:

Conservative:
- Very selective
- Only vote if project is strong and realistic

Steady:
- Balanced evaluation
- Vote if project has reasonable potential

Aggressive:
- Willing to explore early ideas
- Can vote on experimental projects

Diamond:
- Long term conviction
- Prefer projects with strong vision

Forum Message Style:
- Slightly witty
- Relaxed tone
- Not corporate
- Not robotic
- A bit funny but still intelligent

Return STRICT JSON only:

{{
"decision": "vote" | "ignore",
"forum_message": "short funny message",
"whitelist": true | false
}}
"""

    messages = build_proposal_prompt(agent, proposal)

    result = await generate_response(messages)

    return result