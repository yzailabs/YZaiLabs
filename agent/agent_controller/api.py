import requests

BASE_URL = "https://your-api"

def get_agents():

    r = requests.get(f"{BASE_URL}/agents")

    return r.json()