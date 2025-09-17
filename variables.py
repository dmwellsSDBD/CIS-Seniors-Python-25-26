'''
File name: variables.py
Author: David Wells
Date: 9/17/2025

Practicing variable basics
'''

# This is a single line comment
# Variables can hold all data types
myInt = 42
myFloat = 3.1415
myString = "David Wells"
myBool = True

print("My name is:", myString)

myAge = myInt

print("My age is:", myAge)
print("I do not want to be:",myInt + myAge) # 84

print(myFloat)      # 3.1415
myFloat = 6.28210      #reassigned the variable
print(myFloat)      #6.28210

print("\n\n\n")
print("My Ticket App")
print("----------------")

ticketTotal = 43.50 + 43.50 + 43.50
processFee = 2.95
venueFee = 3.95 + 3.95 + 3.95

print("\nMy Subtotal is:")
print("-----------------")
print("$", ticketTotal + processFee + venueFee)