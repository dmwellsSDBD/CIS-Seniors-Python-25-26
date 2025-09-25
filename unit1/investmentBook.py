"""
Program: investmentBook.py
Author: David
Compute an investment report.

Compute an Investment Report
1. The inputs are:
    starting investment amount
    number of years
    Interest rate (an Integer percent)

2. The report is displayed in tabular form with a header
3. Computations and outputs:
    for each year of the investment
        compute the interest and add it to the investment
        print a formatted row of results for that year
4. The ending invesment and interest you have paid in total are also displayed
"""
print("\n\n")
print("=" * 40)
print("My Investment Tracker")
print("=" * 40)

# Accept the Inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initiialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table

print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending balance"))

# Compute and display the results for each year

for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest


# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)
