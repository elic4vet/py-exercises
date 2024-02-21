  
new_item = input('Enter a to-do item: ')
with open('todo.txt', 'w+') as todo_file:
    todo = todo_file.read()
    todo = todo + new_item + '\n'
with open('todo.txt', 'r+') as todo_file:
    todo_file.write(todo)
 
'''  
import csv 

field_names = ['name', 'age']

data = [ 
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Jim', 'age': 35}
]

with open('data.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)
 

import csv

with open('data.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        print(row['name'], row['age'])
 

with open('trees.csv', 'r') as filecsv:
    table = csv.DictReader(filecsv)
    tree_height_list = []
    for row in table:
        print(row)
        tree_height = row['height']
        tree_height_list.append(tree_height)
    smallest_tree = min(tree_height_list)
    print(smallest_tree)
'''

 