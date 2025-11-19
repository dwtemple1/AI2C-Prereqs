# https://github.com/shafe123/AI2C-Prereqs

# more on data types
# reference documentation:  https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/reference/expressions.html#operator-summary

### booleans
# determine if the following statement is true or false
# you can test these in the interpreter or using print statements
True and True # True
False and True # False
True or False # True
False and True or False # False
False and (True or False) # False

### converting data types
# what is the difference between implicit and explicit type conversion?
# determine if the following statements result in errors or not
5 + '5' # error
5 + int('5') # 10, explicit type conversion
int(5.2) + int('5') # 10.2, explicit type conversion
5.2 + float('5') # 10.2, explicit type conversion
5 and '5' # bonus question, does this evaluate to true or false?; '5', would evaluate to true because both are "non-empty"
[1, 2] or [3, 4] # bonus question, does this evaluate true or false?; [1, 2], would evaluate to true because one is non-empty
True + 5 # 6, implicit type conversion
False + 5 # 5, implicit type conversion

my_guess = input('Enter a guess')
print('10 times your guess is ' + 10 * my_guess) # be careful as input() returns a string...

# can you see how implicit conversions can get you in trouble...?

### binary and hexadecimal
# Convert 10 to binary
bin(10)
# Convert 255 to binary
bin(255)
# Convert 0b10101 to decimal
int('0b10101', 2)
# Convert 0x10101 to decimal
int('0x10101', 16)
# Perform a bitwise 'or' between 0b110101 and 0b101010, what is its decimal value
int('0b110101', 2) | int('0b101010', 2)
# Perform a bitwise 'or' between 53 and 42, what is its binary value
bin(53 | 42)

# Do the same with a bitwise 'and'
int('0b110101', 2) & int('0b101010', 2)
bin(53 & 42)

### string manipulation
# Convert 'hello' to bytes and then convert the bytes to an integer
# hint: use the encode method
int('hello'.encode(), 2)

# What's the difference between strip and replace?  When might you use both?
# strip only removes leading or trailing characters
# replace with replace all instances of the first argument with the second argument
# replace is useful for removing values anywhere within the string
# strip is useful if you know the values are at the beginning or end

# Use index, len, slicing, and concatenation to 
# replace the word 'horrible' with 'beautiful'
# "It's a horrible day."
# "It's a beautiful day."
"It's a horrible day.".replace("horrible", "beautiful")

# scan through the 'is____' string methods in the documentation.
# how might you use those methods to clean a dataset?
# you could loop through each of the words or characters and use those methods to 
# determine which things you want to remove or change
my_str = 'hello, I put some; weird"" stuff in here'
result_list = [] # accumulate the "good" characters here
for character in my_str:
    if character.isalpha() or character.isspace(): # only keep alpha-numeric characters and spaces
        result_list.append(character)
result_str = ''.join(result_list) # join the list back to a string
# remember how strings are immutable and lists are mutable...
# it is memory/compute expensive to build many, many strings (talking thousands - millions of characters)