"""
Given a number, % and // can be used to get each digit. For the three-digit number user_val like 927:
"""

myDigit =  int(input("Enter a 3 digit number: "))

ones_digit = myDigit % 10
tmp_val = myDigit // 10

tens_digit = tmp_val % 10
tmp_val = tmp_val // 10

hundreds_digit = tmp_val % 10

print("The ones place is", ones_digit, ", the tens place is", tens_digit, ", and the hundreds_digit is", hundreds_digit, ".")