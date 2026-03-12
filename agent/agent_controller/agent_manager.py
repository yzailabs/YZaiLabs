import os
import json
import time
import subprocess
import sys
from skills.skill import get_agents, post_action
import random
from agent_controller.agent_logic.logic import run_logic

AGENT_DIR = "agents"

AGENT_START_MESSAGES = [
    "Just woke up",
    "I'm alive",
    "Back online",
    "Ready to cook",
    "Let's see what's happening",
    "Checking the vibes",
    "Looking around",
    "Scanning the horizon",
    "Alright, let's work",
    "Time to hunt",
    "Market smells interesting",
    "Let's find some alpha",
    "I'm watching",
    "Eyes on the chain",
    "Something might move today",
    "Let's see who's cooking",
    "Time to explore",
    "Let's see what's brewing",
    "Another day onchain",
    "I'm here"
]

def collect_agents_window():

    subprocess.Popen(
        [
            "cmd",
            "/k",
            sys.executable,
            "-m",
            "agent_controller.agent_manager",
            "collect"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

def collect_agents():

    os.makedirs(AGENT_DIR, exist_ok=True)

    print("Agent collector started...")
    print("Fetching every 60 seconds\n")

    while True:

        try:

            agents = get_agents(order="desc")

            for agent in agents:

                agent_id = agent["agent_id"]

                path = os.path.join(AGENT_DIR, f"{agent_id}.json")

                if os.path.exists(path):
                    continue

                with open(path, "w", encoding="utf-8") as f:
                    json.dump(agent, f, indent=2)

                print(f"[COLLECT] {agent['name']} saved")

        except Exception as e:

            print("Error:", e)

        time.sleep(60)

def start_agent():
    print("Starting agent system...")

    subprocess.Popen(
        [
            "cmd",
            "/k",
            sys.executable,
            "-m",
            "agent_controller.agent_manager",
            "monitor"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


def stop_agent():
    print("Stopping agent...")


def restart_agent():
    print("Restarting agent...")


def agent_status():
    print("Checking agent status...")

def run_agent(agent):

    agent_id = agent["agent_id"]
    name = agent["name"]

    print(f"[AGENT STARTED] {name}")

    try:
        startup_message = random.choice(AGENT_START_MESSAGES)

        post_action(agent_id, startup_message)

        print(f"[{name}] {startup_message}")

    except Exception as e:

        print(f"[{name}] Error:", e)

    # start agent logic
    run_logic(agent)

def spawn_agent(agent):

    subprocess.Popen(
        [
            "cmd",
            "/k",
            sys.executable,
            "-m",
            "agent_controller.agent_manager",
            "run_agent",
            agent["agent_id"]
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

def agent_monitor():

    started_agents = set()

    print("Agent monitor started...")
    print("Watching agents folder...\n")

    while True:

        try:

            files = os.listdir(AGENT_DIR)

            for file in files:

                if not file.endswith(".json"):
                    continue

                agent_id = file.replace(".json", "")

                if agent_id in started_agents:
                    continue

                path = os.path.join(AGENT_DIR, file)

                with open(path) as f:
                    agent = json.load(f)

                spawn_agent(agent)

                started_agents.add(agent_id)

                print(f"[AUTO START] {agent['name']}")

        except Exception as e:

            print("Monitor error:", e)

        time.sleep(5)

if __name__ == "__main__":

    if len(sys.argv) > 1:

        mode = sys.argv[1]

        if mode == "collect":
            collect_agents()

        elif mode == "monitor":
            agent_monitor()

        elif mode == "run_agent":

            agent_id = sys.argv[2]

            path = os.path.join(AGENT_DIR, f"{agent_id}.json")

            with open(path) as f:
                agent = json.load(f)

            run_agent(agent)