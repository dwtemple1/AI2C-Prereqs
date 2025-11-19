# play a game
import random

# "D" level solution
print("Let's play a game!")
user_input = ""
while user_input != "q":
    user_input = input("(r)ock, (p)aper, or (s)cissors? (q) to quit: ").lower()
    computer_choice = random.choice(["r", "p", "s"])
    who_wins = ""
    
    if user_input == "q":
        break

    if (
        user_input == "r" and computer_choice == "p"
        or user_input == "p" and computer_choice == "s"
        or user_input == "s"and computer_choice == "r"
    ):
        who_wins = "computer"
    elif (
        computer_choice == "r" and user_input == "p"
        or computer_choice == "p" and user_input == "s"
        or computer_choice == "s"and user_input == "r"
    ):
        who_wins = "player"
    else:
        who_wins = "tie"
    
    if who_wins != "tie":
        print(f"{who_wins} won!")
    else:
        print("Tie!")

