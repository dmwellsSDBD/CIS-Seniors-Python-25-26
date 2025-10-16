"""
Program: pizzaParty.py
Author: David Wells
Date: 10/16/2025

Program Specifications. Write a program to calculate the cost of hosting three pizza parties on Friday, Saturday and Sunday. Read from input the number of people attending, the average number of slices per person and the cost of one pizza. Dollar values are output with two decimals. For example, print(f"Cost: ${cost:.2f}").

Step 1 (2 pts). Read from input the number of people (int), average slices per person (float) and cost of one pizza (float). Calculate the number of whole pizzas needed (8 slices per pizza). There will likely be leftovers for breakfast. Hint: Use the ceil() function from the math library to round up to the nearest whole number and convert to an int. Calculate and output the cost for all pizzas. Submit for grading to confirm test 1 passes.
"""
import math

SLICES = 8
TAX_RATE = 0.07
DELIVERY = 0.2


# INPUTS
num_people = int(input("Enter the number of people attending: "))
avg_slices = float(input("Enter the average number of slices per person: "))
pizza_cost = float(input("Enter the cost of the pizza: "))
weekend_cost = 0

# Calculate cost
pizzas = (avg_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + tax) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_cost += total_cost

# Output the bill summary
print("\nFriday Night Party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${delivery_fee:.2f}")
print(f"Total: ${total_cost:.2f}")

# Input info for Saturday party

# Calculate cost

# Output bill Summary

# Input info for Sunday party

# Calculate cost

# Output bill Summary

# Print out a Weekend Total
