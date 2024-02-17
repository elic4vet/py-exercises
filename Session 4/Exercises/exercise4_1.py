'''Exercise 4.1
When I'm travelling in the winter I often forget to pack warm clothes. Let's write a program to help
me to remember the right clothes.
The program should check if the first item in the clothes list is "shorts". If it is it should change the
value to "warm coat".'''


clothes = [

"shorts",
"shoes",
"t-shirt",
]

if clothes[0] == "shorts":
   clothes[0] = "warm coat"
print(clothes)