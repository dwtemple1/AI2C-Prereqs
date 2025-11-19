# how many games to play
# only accept odd games
# keep track of games
# validate input
import random

# "A" level solution
print("Let's play a game!")
game_max = 0
while game_max % 2 == 0 or game_max < 1 or game_max > 9:
    try:
        print("Can only enter odd games to be able to determine a winner!")
        user_input = input("How many times would you like to play? (q to quit) ")
        if user_input == "q":
            exit()
        game_max = int(user_input)
    except ValueError:
        continue
game_count = 0
stats = { "computer": 0, "player": 0, "tie": 0 }

player_choice = ""
winning_plays = [("p", "r"), ("s", "p"), ("r", "s")]
while player_choice != "q" and game_count < game_max:
    player_choice = input("(r)ock, (p)aper, or (s)cissors? (q) to quit: ").lower().strip()
    
    if player_choice not in ["q", "p", "s", "r"]:
        print("Enter a valid choice...")
        continue
    if player_choice == "q":
        break

    computer_choice = random.choice(["r", "p", "s"])
    print(f"Computer chose: {computer_choice}.")
    who_wins = ""

    if (computer_choice, player_choice) in winning_plays:
        who_wins = "computer"
        stats["computer"] += 1
    elif (player_choice, computer_choice) in winning_plays:
        who_wins = "player"
        stats["player"] += 1
    else:
        who_wins = "tie"
        stats["tie"] += 1
        game_count -= 1 # ties don't count towards games played
    
    if who_wins != "tie":
        print(f"{who_wins} won!")
    else:
        print("Tie!")
    print()

    if stats["computer"] > game_max // 2 or stats["player"] > game_max // 2:
        print(f"Overall winner: {who_wins}!!!")
        break

print("Game stats: ")
for key, value in stats.items():
    print(f"{key.capitalize()}: {value} games")
