'''Write a program that simulates a lottery. 
The program should have a list of seven numbers that
represent a lottery ticket. It should then generate seven random numbers. After comparing the two
sets of numbers, the program should output a prize based on the number of matches:

● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers'''

import random

lottery_numbers = ["1","2","3","4","5","6","7"]
random_numbers = []

for i in range(7):
    random_numbers.append(random.randint(1, 7))

count = 0

for i in range(7):
    if lottery_numbers[i] == str(random_numbers[i]):
        count += 1

if count == 3:
    prize = "£20"
elif count == 4:
    prize = "£40"
elif count == 5:
    prize = "£100"
elif count == 6:
    prize = "£10000"
elif count == 7:
    prize = "£1000000"
else:
    prize = "0"

print(f"You matched {count} numbers. Your prize is {prize}.")
