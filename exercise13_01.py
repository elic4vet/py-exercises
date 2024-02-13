'''  
Exercise 1: Prime Number Checker
Write a Python program that prompts the user to enter a positive integer. 

Check if the entered number is a prime number or not. Implement an efficient 
algorithm to handle larger numbers.
'''
number = int(input("Enter a positive integer: "))
if number > 1:  #check if the number is greater than 1
    for i in range(2, number):  #check if the number is divisible by any number other than 1 and itself
        if (number % i) == 0: #if the number is divisible by any number other than 1 and itself, it is not a prime number
            print("The number is not a prime number")
            break #exit the loop
    else:
        print("The number is a prime number") #if the number is not divisible by any number other than 1 and itself, it is a prime number
else:
    print("The number is not a prime number") #if the number is less than 1, it is not a prime number

