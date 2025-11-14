import random
random.seed(1234)

def make_choice():
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")

    while True:
        choice = input("Your choice: ")
        if (choice.isnumeric() == False) or (choice not in ["1", "2", "3", "0"]):
            print("Invalid choice! Try again.")
        else:
            return int(choice)
        
def rps(player_name, player_choice):
    options = {
        1: "rock",
        2: "paper",
        3: "scissors"
    }

    ascii_art = {
        "rock": """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        "paper": """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
        "scissors": """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    }

    print("#########################")

    player_choice = options[player_choice]

    print(f"{player_name} chose {player_choice}.\n")
    print(ascii_art[player_choice])

    print("#########################")

    cpu_choice = random.randint(1, 3)
    cpu_choice = options[cpu_choice]

    print(f"RPS-3PO chose {cpu_choice}.")
    print(ascii_art[cpu_choice])

    print("#########################")

    return player_choice, cpu_choice

def who_wins(player_name, player_choice, cpu_choice, player_score, cpu_score):
    winning_cases = { # scissors beats rock, scissors beats paper, paper beats rock
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if player_choice == cpu_choice:
        print(f"It's a draw! Both players chose {player_choice}")
        player_score["pd"] += 1
        cpu_score["cd"] += 1
    elif winning_cases[player_choice] == cpu_choice:
        print(f"{player_name} {player_choice} beats RPS-3PO {cpu_choice}.")
        player_score["pw"] += 1
        cpu_score["cl"] += 1
    elif winning_cases[cpu_choice] == player_choice:
        print(f"RPS-3PO {cpu_choice} beats {player_name} {player_choice}.")
        player_score["pl"] += 1
        cpu_score["cw"] += 1

def print_score(player_name, player_score, cpu_score):
    print("Results:")

    print(f"{player_name} - wins ({player_score["pw"]}), losses ({player_score["pl"]}), draws ({player_score["pd"]})")
    print(f"RPS-3PO - wins ({cpu_score["cw"]}), losses ({cpu_score["cl"]}), draws ({cpu_score["cd"]})")

    print()

def main():
    # initialize results counters (pw = player win, pw = player lose, pd = player draw + same for cpu)
    player_score = {
        "pw": 0,
        "pl": 0,
        "pd": 0,
    }

    cpu_score = {
        "cw": 0,
        "cl": 0,
        "cd": 0
    }

    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!\n")

    player_name = input("Insert player name: ")

    print(f"Welcome, {player_name}!\n")

    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    while True:
        player_choice = make_choice()

        if player_choice == 0:
            break

        print("Rock! Paper! Scissors! Shoot!\n")

        player_choice, cpu_choice = rps(player_name, player_choice)

        who_wins(player_name, player_choice, cpu_choice, player_score, cpu_score)

        print_score(player_name, player_score, cpu_score)

    print("\nProgram ending.")


if __name__ == "__main__":
    main()