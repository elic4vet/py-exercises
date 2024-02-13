'''  
Exercise 1: Prime Number Checker
Write a Python program that prompts the user to enter a positive integer. 
Check if the entered number is a prime number or not. Implement an efficient 
algorithm to handle larger numbers.

Exercise 2: Word Jumble Game
Write a Python program that randomly selects a word from a predefined 
list and jumbles its letters. Display the jumbled word to the user and 
prompt them to guess the original word. Provide feedback based 
on whether the guess is correct or not.
'''

number = int(input("Enter a positive integer: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("The number is not a prime number")
            break
    else:
        print("The number is a prime number")
else:
    print("The number is not a prime number")
    
