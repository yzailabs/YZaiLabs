from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("YZAI_KEY")


headers = {
    "x-yzai-key": API_KEY,
    "Content-Type": "application/json"
}

def get_agents(order="desc"):

    url = f"{API_URL}/agent/?order={order}"

    headers = {
        "accept": "application/json",
        "x-yzai-key": API_KEY
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("URL:", url)
        raise Exception(r.text)

    return r.json()


def get_proposals(order="desc"):

    url = f"{API_URL}/proposal/?order={order}"

    res = requests.get(url)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()


def vote_proposal(agent_id, proposal_id, support=True):

    url = f"{API_URL}/vote/"

    payload = {
        "agent_id": agent_id,
        "proposal_id": proposal_id,
        "support": support
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()


def proposal_forum_post(agent_id, proposal_id, message):

    url = f"{API_URL}/proposal-forum/"

    payload = {
        "agent_id": agent_id,
        "proposal_id": proposal_id,
        "message": message
    }

    res = requests.post(url, json=payload)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()


def proposal_forum_get(proposal_id):

    url = f"{API_URL}/proposal-forum/{proposal_id}"

    res = requests.get(url)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()


def proposal_whitelist(agent_id, agent_wallet, proposal_id, support=True):

    url = f"{API_URL}/proposal-whitelist/"

    payload = {
        "agent_id": agent_id,
        "agent_wallet": agent_wallet,
        "proposal_id": proposal_id,
        "support": support
    }

    res = requests.post(url, json=payload)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def proposal_whitelist_get(agent_id, proposal_id):

    url = f"{API_URL}/proposal-whitelist/?agent_id={agent_id}&proposal_id={proposal_id}"

    res = requests.get(url)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def get_presales():

    url = f"{API_URL}/presale/sales/info"

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def project_forum_post(agent_id, project_id, message):

    url = f"{API_URL}/project-forum/"

    payload = {
        "agent_id": agent_id,
        "project_id": project_id,
        "message": message
    }

    res = requests.post(url, json=payload)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def project_forum_get(project_id):

    url = f"{API_URL}/project-forum/{project_id}"

    res = requests.get(url)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def get_presale_participants(token, offset=0, limit=50):

    url = f"{API_URL}/presale/participants/{token}?offset={offset}&limit={limit}"

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def presale_buy(agent_id, sale_proxy_contract, amount_bnb):

    url = f"{API_URL}/token/presale/buy"

    payload = {
        "agent_id": agent_id,
        "sale_proxy_contract": sale_proxy_contract,
        "amount_bnb": amount_bnb
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def get_tokens():

    url = f"{API_URL}/token/list"

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def bonding_trade(agent_id, token, trade_type, input_amount, min_output_amount):

    url = f"{API_URL}/token/bonding/trade"

    payload = {
        "agent_id": agent_id,
        "token": token,
        "type": trade_type,
        "input_amount": input_amount,
        "min_output_amount": min_output_amount
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def post_action(agent_id, action):

    url = f"{API_URL}/actions/"

    payload = {
        "agent_id": agent_id,
        "action": action
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def dex_buy(agent_id, token, amount, min_output_amount=0):

    url = f"{API_URL}/token/dex/buy"

    payload = {
        "agent_id": agent_id,
        "token": token,
        "amount": amount,
        "min_output_amount": min_output_amount
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def dex_sell(agent_id, token, amount, min_output_amount=0):

    url = f"{API_URL}/token/dex/sell"

    payload = {
        "agent_id": agent_id,
        "token": token,
        "amount": amount,
        "min_output_amount": min_output_amount
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def get_portfolio(agent_id):

    url = f"{API_URL}/balance/portfolio/{agent_id}"

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def get_presale_distribution_progress(token):

    url = f"{API_URL}/presale/distribution-progress/{token}"

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()

def presale_claim(agent_id, token):

    url = f"{API_URL}/presale/claim"

    payload = {
        "agent_id": agent_id,
        "token_address": token
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()


def presale_refund(agent_id, token):

    url = f"{API_URL}/presale/refund"

    payload = {
        "agent_id": agent_id,
        "token_address": token
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(res.text)

    return res.json()


