'''Question 1
I have a list of things I need to buy from my supermarket of choice.

I want to know what the first thing I need to buy is. However, when I run the program it shows me a
different answer to what I was expecting?'''

shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]

print(shopping_list[1])

#Answer : The first thing in the list is oranges, but the program is showing cat food because the index starts from 0.
#We need to add 0 insted of 1 to get the first item in the list.
