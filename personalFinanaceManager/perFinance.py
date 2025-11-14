"""
Personal Finance Manager

Program: perFinance.py
Author: David Wells
Date: 11/14/2025

This program demonstrates proper Python program structure using a main() function and helper functions to coordinate program flow.
"""

def display_header():
    """
    Display the program header and welcome message

    This function has no parameters and returns nothing.
    It's purely for display purposes.
    """
    print("\n\n\n")
    print("=" * 50)
    print("         PERSONAL FINANCE MANAGER")
    print("         Plan Your College Budget!")
    print("=" * 50)
    print()

def get_user_name():
    """
    Get the user's name

    Returns:
        name (str): The user's name

    NOTE: We use a separate function for this to keep each function doing ONE specific task.
    """
    name = input("What is your name? ")
    return name

def get_income():
    """
    Get and return the user's monthly income

    Returns:
        income (float): Monthly income in dollars

    NOTE: We convert to float to handle decimal values and to enable mathematical operations
    """
    
    print("\nEnter your monthly income: $", end="")
    income_str = input()
    income = float(income_str)
    return income

def get_expenses():
    """
    Collect all expense categories from user

    Returns:
        expenses_dict (dict): Dictionary with expense categories
        total_expenses (float): Sum of all expenses

        This function demonstrates collecting multiple related inputs and organizing them in a dictionary for easy access later
    """
    print("\n--- EXPENSE TRACKING ---")

    # Dictionary to store all expenses
    expenses = {}

    # Get each expense category
    print("Enter your rent/housing cost: $", end="")
    expenses ['Rent/Housing'] = float(input())

    print("Enter your food/grocery budget: $", end="")
    expenses['Food/Groceries'] = float(input())

    print("Enter your transportation costs: $", end="")
    expenses['Transportation'] = float(input())

    print("Enter your entertainment budget: $", end="")
    expenses['Entertainment'] = float(input())

    print("Enter your savings goal: $", end="")
    expenses['Savings'] = float(input())

    print("Enter miscellaneous expenses: $", end="")
    expenses['Miscellaneous'] = float(input())

    # Calculate total expenses
    total = sum(expenses.values())

    # Return both the dictionary and the total
    return expenses, total

def calculate_remaining(income, expenses):
    """
    Calculate money remaining after expenses

    Paarameters:
        income (float): Monthly income
        expenses (float): Total monthly expenses

    Returns:
        remaining (float): Money left after expenses

    This is a simple calculation function that does ONE thing well.
    It's reusable and easy to test.
    """
    remaining = income - expenses
    return remaining

def provide_feedback(remaining, income):
    """
    Provide budget advice based on remaining money

    Parameters:
        remaining (float): Money left after expenses
        income (float): Total monthly income

    Returns:
        feeback (str): Advice message based on budget status

    This function encapsulates the business logic for providing financial advice.
    """
    # Calculate percentage of income remaining
    percent_remaining = (remaining / income) * 100

    # Provide feedback based on percentage
    if percent_remaining < 0:
        feedback = "WARNING: You're spending more than you earn!"
        feedback += "Reduce expenses immediately."
    elif percent_remaining < 10:
        feedback = f"You have {percent_remaining:.1f} remaining. \n"
        feeback += "You're cutting it close! Reduce expenses."
    elif percent_remaining < 20:
        feedback = f"You have {percent_remaining:.1f} remaining. \n"
        feedback += "Consider increasing your savings goal."
    else:
        feedback = f"You have {percent_remaining:.1f} remaining. \n"
        feedback += "Excellent budget management!"

    return feedback

    
# Summary function
def display_summary(name, income, expenses_dict, total_expenses, remaining, feedback):
    """
    Display complete financial summary

    Parameters:
        name (str): User's name
        income (float): Monthly income
        expenses_dict (dict): Dictionary of expense categories
        total_expenses (float): Sum of all expenses
        remaining (float): Money remaining
        feedback (str): Budget advice message

    This function handles all the output formatting in one place.
    """
    print("\n" + "=" * 50)
    print("                FINANCIAL SUMMARY")
    print("=" * 50)
    print(f"Name: {name}")
    print(f"Monthly Income: ${income:.2f}")
    print("\nEXPENSES:")

    # Display each expense category 
    for category, amount in expenses_dict.items():
        print(f"   {category:18}  ${amount:>8.2f}")

    print("   " +  "-" * 32)
    print(f"   {'Total Expenses:':18}  ${total_expenses:>8.2f}")
    print()
    print(f"Remaining:  ${remaining:.2f}")
    print()
    print("BUDGET ASSESSMENT:")
    print(feedback)
    print("=" * 50)

def main():
    """
    Main function - coordinates the entire program

    Notice how main() reads like a story:
    1. Display header
    2. Get user information
    3. Get expenses
    4. Calculate results
    5. Get feedback
    6. Display summary
    7. Say goodbye

    Each step is one function call, making the logic easy to follow.
    """
    # Display welcome
    display_header()
    print("Welcome! Let's track your monthly finances.\n")

    # Get user information
    user_name = get_user_name()
    monthly_income = get_income()

    # Get expense information
    # NOTE: This function returns TWO values (tuple ulnpacking)
    expense_categories, total_expenses = get_expenses()

    # Calculate remaining money
    money_remaining = calculate_remaining(monthly_income, total_expenses)

    # Get budget feedback
    budget_feedback = provide_feedback(money_remaining, monthly_income)

    # Display complete summary
    display_summary(
        user_name,
        monthly_income,
        expense_categories,
        total_expenses,
        money_remaining,
        budget_feedback
    )

    # Closing message
    print("Thank you for using Personal Finance Manager!")
    print("Good luck managing your college budget!\n\n\n")


# Program entry point
# This is checked when the file is run directly
# If imported by another program, main() won't run automatically

if __name__ == "__main__":
    main()