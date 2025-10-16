"""
Program: carpetSales.py
Author: David Wells
Date: 10/16/2025

Step 1: Read from input the carpet price per square foot (float), room width (int) and room length (int). Calculate the room area in square feet. Calculate the carpet price based on square feet with an additional 20% for waste. Output square feet and carpet cost. Submit for grading to confirm 1 test passes.
"""

# initialize Constants
TAX_RATE = 0.07
WASTE_PCT = 1.2
LABOR_RATE = 0.75

totalSales = 0

# Order #1
# Input price per sq foot, room width and room length
price = float(input("Enter the price per square foot: "))
width = int(input("Enter the width of the room: "))
length = int(input("Enter the length of the room: "))

# Calculate room square feet
sq_feet = width * length

# Calculate carpet cost including 20% waste
carpet = (sq_feet * WASTE_PCT) * price

# Calculate labor (0.75 per sq ft)
labor = sq_feet * LABOR_RATE

# Calculate sales tax (7%)
tax = (carpet + labor) * TAX_RATE

# Calculate total cost
cost = carpet + tax + labor

# Output results
print("Order #1")
print(f"Square Footage: {sq_feet} sq ft")
print(f"Carpet Cost: ${carpet:.2f}")
print(f"Labor: ${labor:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost

# Order 2

# Input
print("\nFor order 2, add the price per sq ft, width, and length all separated by a space. Ex. 2.45 16 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)

# Calculations
sq_feet = width * length
carpet = (sq_feet * WASTE_PCT) * price
labor = (sq_feet * LABOR_RATE)
tax = (carpet + labor) * TAX_RATE
cost = carpet + tax + labor

# Output results
print("Order #2")
print(f"Square Footage: {sq_feet} sq ft")
print(f"Carpet Cost: ${carpet:.2f}")
print(f"Labor: ${labor:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost

# Order 3
# Input
print("\nFor order 3, add the price per sq ft, width, and length all separated by a space. Ex. 2.45 16 10")
price, width, length = input().split()
price = float(price)
width = int(width)
length = int(length)

# Calculations
sq_feet = width * length
carpet = (sq_feet * WASTE_PCT) * price
labor = (sq_feet * LABOR_RATE)
tax = (carpet + labor) * TAX_RATE
cost = carpet + tax + labor

# Output results
print("Order #3")
print(f"Square Footage: {sq_feet} sq ft")
print(f"Carpet Cost: ${carpet:.2f}")
print(f"Labor: ${labor:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Cost: ${cost:.2f}")
totalSales += cost

# Output total sales
print(f"\nYour total carpet sale is: ${totalSales:.2f}")