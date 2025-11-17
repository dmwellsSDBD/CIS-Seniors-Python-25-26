def display_welcome():
    """Display program header"""
    print("=" * 50)
    print("COLLEGE APPLICATION TRACKER")
    print("=" * 50)
    print()

def get_college_count():
    """Get number of colleges user is applying to"""
    count_str = input("How many colleges are you applying to? ")
    count = int(count_str)
    return count

def get_application_costs(num_colleges):
    """Calculate total application costs"""
    cost_per_app = 50.00  # Average application fee
    total_cost = num_colleges * cost_per_app
    return total_cost

def get_sat_score():
    """Get user's SAT score"""
    score_str = input("What is your SAT score? ")
    score = int(score_str)
    return score

def analyze_sat(score):
    """Provide feedback on SAT score"""
    if score >= 1400:
        return "Excellent! Very competitive for top schools."
    elif score >= 1200:
        return "Good score! Competitive for many universities."
    elif score >= 1000:
        return "Solid foundation. Consider retaking for better options."
    else:
        return "Consider retaking to improve college options."

def display_summary(colleges, cost, sat_score, sat_feedback):
    """Display complete application summary"""
    print("\n" + "=" * 50)
    print("YOUR APPLICATION SUMMARY")
    print("=" * 50)
    print("Number of colleges: " + str(colleges))
    print("Total application cost: $" + str(cost))
    print("SAT Score: " + str(sat_score))
    print("Assessment: " + sat_feedback)
    print("=" * 50)

def main():
    """Main function - orchestrates the entire program"""
    # Welcome the user
    display_welcome()
    
    # Collect information
    num_colleges = get_college_count()
    total_cost = get_application_costs(num_colleges)
    sat = get_sat_score()
    
    # Analyze data
    feedback = analyze_sat(sat)
    
    # Display results
    display_summary(num_colleges, total_cost, sat, feedback)
    
    print("\nGood luck with your applications!")

# Entry point - program starts here
if __name__ == "__main__":
    main()