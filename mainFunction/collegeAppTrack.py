def display_welcome():
    """Display program header"""

def get_college_count():
    """
    Get number of colleges user is applying to
    Return
        count (int)
    """

def get_application_costs(num_colleges)
    """
    Calculate total application costs

    Return
        total_cost (float)
    """

def get_sat_score():
    """
    Get user's SAT score

    Return:
        score (int)
    """

def analyze_sat(score):
    """
    Provide feedback on SAT score
    >= 1400 - Excellent
    >= 1200 - Good score
    >= 1000 - Solid foundation
    else - Consider retaking to improve college options.
    """

def display_summary(colleges, cost, sat_score, sat_feedback):
    """
    Display complete application summary with header
    """

def main():
    """Main function - orchestrates the entire progam"""
    # Welcome the user
    display_welcome()

    # collect information
    num_colleges = get_college_count()
    total_cost = get_application_costs(num_colleges)
    sat = get_sat_score()

    # Analyze data
    feedback = analyze_sat(sat)

    # Display results
    display_summary(num_colleges, total_cost, sat, feedback)

    print("\nGood luck with your")

# entry point
if __name__ == __main__:
    main()