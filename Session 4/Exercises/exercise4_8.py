
''' Exercise 4.8
Write a program to create a random name. You should have a list of random first names and a list of
last names. Choose a random item from each and display the result.'''

random_firstNames = ["John", "Jane", "Jack", "Jill", "James", "Jenny","Jasmine"]
random_lastNames = ["Smith", "Johnson", "Williams", "Davis", "Wilson", "Moore", "Taylor"]

import random 

random_name =  random.choice(random_firstNames) + " " + random.choice(random_lastNames)

print(random_name)