from agent_controller.banner import show_banner
from agent_controller.menu import main_menu
from agent_controller import agent_manager
from agent_controller import wallet


def run():

    show_banner()

    while True:

        choice = main_menu()

        if choice == "Collect Agents":
            agent_manager.collect_agents_window()
            
        elif choice == "Start Agent":
            agent_manager.start_agent()

        elif choice == "Stop Agent":
            agent_manager.stop_agent()

        elif choice == "Restart Agent":
            agent_manager.restart_agent()

        elif choice == "Agent Status":
            agent_manager.agent_status()

        elif choice == "Analyze Token / Memecoin":
            print("Analyzing token...")

        elif choice == "Wallet":
            wallet.show_wallet()

        elif choice == "Exit":
            break


if __name__ == "__main__":
    run()