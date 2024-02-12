''' Exercise 3.8
Not Quite Roulette
Ask the user to enter the following three things using input():

● The amount they want to bet
● A colour (red or black)
● A number between 1 and 100
'''
'''
After generating a random number and colour:
● If the colour matches, the users keeps the amount that was bet
● If the number matches, the users wins double the amount that was bet 
● If the colour and number matches, the users wins 100 times the amount that was bet 
● When neither the colour or number matches the user wins 0
● Output the amount the user won

'''

bet_amount= int(input("Enter the amount you want to bet: "))
colour_choice = input("Enter the colour you want to bet on: ")
number_choice = int(input("Enter the number you want to bet on: "))



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

if random_colour == colour_choice:
    print("You won the amount that was bet: ", bet_amount)
    winning_amount = bet_amount

elif random_number == number_choice:
    print("You won double the amount that was bet: ", bet_amount*2)
    winning_amount = bet_amount*2

elif random_colour == colour_choice and random_number == number_choice:
    print("You won 100 times the amount that was bet: ", bet_amount*100)
    winning_amount = bet_amount*100
else:
    print("You won 0")
    winning_amount = 0

print("Amount you won: ", winning_amount)
