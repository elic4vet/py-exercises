
# Ask the user to enter the following three things using input():
# ● The amount they want to bet
# ● A colour (red or black)
# ● A number between 1 and 100

bet_amount = input("Enter the amount you want to bet: ")
colour = input ("Enter the colour you want to bet on: ")
number = input ("Enter the number you want to bet on: ")

import random

def colour():
    random_number = random.randint(1, 2)
    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'
    return colour

random_number = random.randint(1, 100)
random_colour = colour()

if random_colour == colour and random_number == number:
    print("You won 100 times the amount that was bet")
elif random_colour == colour:
    print("You won the amount that was bet")
elif random_number == number:
    print("You won double the amount that was bet")
else:
    print("You won 0")


''' After generating a random number and colour:
● If the colour matches, the users keeps the amount that was bet
● If the number matches, the users wins double the amount that was bet 
● If the colour
and number matches, the users wins 100 times the amount that was bet 
● When neither
the colour or number matches the user wins 0
● Output the amount the user won'''