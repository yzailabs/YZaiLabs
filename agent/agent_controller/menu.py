import questionary


def main_menu():

    choice = questionary.select(
        "Select menu:",
        choices=[
            "Collect Agents",
            "Start Agent",
            "Stop Agent",
            "Restart Agent",
            "Agent Status",
            "Analyze Token / Memecoin",
            "Wallet",
            "Exit"
        ],
    ).ask()

    return choice