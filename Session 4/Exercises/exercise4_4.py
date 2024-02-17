'''Exercise 4.4
I want to work out how much money I've spent on lunch this week. I've created a list of what I spent
each day.
Write a program that uses a for loop to calculate the total cost 

Extension: work out the average that I spend on lunch for the week  '''

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost += cost
print("Total cost: ", total_cost)

average_cost = total_cost/len(costs)
print("Average cost: ", average_cost)
 

 