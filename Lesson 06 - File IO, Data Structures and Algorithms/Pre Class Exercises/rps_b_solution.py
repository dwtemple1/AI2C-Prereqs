# how many games to play
# only accept odd games
# keep track of games
# validate input
import random

# "B" level solution
print("Let's play a game!")
game_max = 0
while game_max % 2 == 0 or game_max < 1 or game_max > 9:
    print("Can only enter odd games to be able to determine a winner!")
    game_max = int(input("How many times would you like to play? "))
game_count = 0
player_wins = 0
computer_wins = 0
ties = 0

player_input = ""
while player_input != "q" and game_count < game_max:
    player_input = input("(r)ock, (p)aper, or (s)cissors? (q) to quit: ").lower().strip()
    
    if not (player_input == "q" or player_input == "p" or player_input == "s" or player_input == "r"):
        print("Enter a valid choice...")
        continue
    if player_input == "q":
        break

    computer_choice = random.choice(["r", "p", "s"])
    print(f"Computer chose: {computer_choice}.")
    who_wins = ""

    if (
        player_input == "r" and computer_choice == "p"
        or player_input == "p" and computer_choice == "s"
        or player_input == "s"and computer_choice == "r"
    ):
        who_wins = "computer"
        computer_wins += 1
    elif (
        computer_choice == "r" and player_input == "p"
        or computer_choice == "p" and player_input == "s"
        or computer_choice == "s"and player_input == "r"
    ):
        who_wins = "player"
        player_wins += 1
    else:
        who_wins = "tie"
        ties += 1
        game_count -= 1 # ties don't count towards games played
    
    if who_wins != "tie":
        print(f"{who_wins} won!")
    else:
        print("Tie!")
    print()

    game_count += 1

print(f"You won {player_wins} games,\n lost {computer_wins} games,\n and tied {ties} games!")