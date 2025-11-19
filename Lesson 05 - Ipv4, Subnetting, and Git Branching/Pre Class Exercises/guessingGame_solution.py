#Create a guessing game.  Randomly pick a number from 1 to 100 (using the random module).  Continually ask the user to guess the number
#If the user guesses too low, tell them they are too low.  If they are too high, tell them they are too high.  Congratulate
#The user when they guess the number.

#Bonus:  Tell the user how many times they had to guess until they were correct.

import random

random_number = random.randint(1,100)
guess = int(input("Guess a number from 1 to 100:   "))
count = 1

while guess != random_number:
    if guess > random_number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess a number from 1 to 100:   "))
    count += 1
print("Congratulations, you got it!")
print("You got it in ", count, "guesses")