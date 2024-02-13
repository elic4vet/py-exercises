'''
Exercise 2: Word Jumble Game
Write a Python program that randomly selects a word from a predefined 
list and jumbles its letters. 

Display the jumbled word to the user and 
prompt them to guess the original word. Provide feedback based 
on whether the guess is correct or not.
'''
word_list = ['python', 'java', 'csharp', 'ruby', 'javascript', 'html', 'css', 'php', 'swift', 'kotlin']

import random

word = random.choice(word_list) #select a random word from the list
jumbled_word = ''.join(random.sample(word, len(word))) #jumble the letters of the word
print("The jumbled word is: ", jumbled_word) #display the jumbled word
guess = input("Enter your guess: ") #prompt the user to enter their guess
if guess == word: #check if the guess is correct
    print("Congratulations! Your guess is correct") #if the guess is correct, display a message
else:
    print("Sorry! Your guess is incorrect")
 