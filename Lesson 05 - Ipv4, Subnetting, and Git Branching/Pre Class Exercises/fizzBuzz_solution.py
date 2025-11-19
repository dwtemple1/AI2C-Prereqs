#Print the numbers from 1 to 100 except...
#If the number is divisible by 3, print "Fizz"
#If the number is divisible by 5, print "Buzz"
#If the number is divisible by 3 and 5, print "Fizz Buzz"

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)