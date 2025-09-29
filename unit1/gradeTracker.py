# Grade Tracker System - Complete Solution
# Demonstrates: print(), input(), for loops, bounds, augmented assignment

print("=" * 50)
print("        GRADE TRACKER SYSTEM")
print("=" * 50)
print("Welcome to the Grade Tracker!")
print("This program will help you analyze student grades.")
print()

# Get number of students with input validation
while True:
    try:
        num_students = int(input("How many students are in your class? (1-20): "))
        if 1 <= num_students <= 20:
            break
        else:
            print("Please enter a number between 1 and 20.")
    except ValueError:
        print("Please enter a valid number.")

print(f"You will enter grades for {num_students} students.")
print()

# Initialize tracking variables
total_points = 0
highest_score = 0
lowest_score = 100  # Start high so first score becomes minimum
passing_count = 0
student_names = []
student_scores = []

# Main data collection loop - demonstrates proper loop bounds
print("Please enter student information:")
print("-" * 40)

for student_number in range(1, num_students + 1):  # KEY: range(1, n+1) avoids off-by-one
    print(f"Student #{student_number}:")
    
    # Get student information
    name = input("  Enter student name: ").strip()
    
    # Get score with validation
    while True:
        try:
            score = float(input("  Enter test score (0-100): "))
            if 0 <= score <= 100:
                break
            else:
                print("    Score must be between 0 and 100.")
        except ValueError:
            print("    Please enter a valid number.")
    
    # Store data
    student_names.append(name)
    student_scores.append(score)
    
    # Update statistics using augmented assignment operators
    total_points += score  # Equivalent to: total_points = total_points + score
    
    # Update highest score
    if score > highest_score:
        highest_score = score
    
    # Update lowest score  
    if score < lowest_score:
        lowest_score = score
    
    # Count passing grades (using augmented assignment)
    if score >= 70:
        passing_count += 1
    
    print()  # Spacing for readability

# Calculate final statistics
average_score = total_points / num_students
pass_rate = (passing_count / num_students) * 100

# Grade distribution counting (bonus feature)
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

# Count grades using another loop with proper bounds
for i in range(len(student_scores)):  # range(len()) is correct here - no off-by-one
    score = student_scores[i]
    if score >= 90:
        grade_counts["A"] += 1
    elif score >= 80:
        grade_counts["B"] += 1
    elif score >= 70:
        grade_counts["C"] += 1
    elif score >= 60:
        grade_counts["D"] += 1
    else:
        grade_counts["F"] += 1

# Display comprehensive results
print("=" * 60)
print("        GRADE ANALYSIS RESULTS")
print("=" * 60)
print(f"Class Summary:")
print(f"  Total Students: {num_students}")
print(f"  Total Points: {total_points:.1f}")
print(f"  Class Average: {average_score:.2f}%")
print(f"  Highest Score: {highest_score:.1f}%")
print(f"  Lowest Score: {lowest_score:.1f}%")
print(f"  Students Passing (≥70%): {passing_count}/{num_students}")
print(f"  Pass Rate: {pass_rate:.1f}%")
print()

print("Grade Distribution:")
print(f"  A grades (90-100%): {grade_counts['A']}")
print(f"  B grades (80-89%):  {grade_counts['B']}")
print(f"  C grades (70-79%):  {grade_counts['C']}")
print(f"  D grades (60-69%):  {grade_counts['D']}")
print(f"  F grades (0-59%):   {grade_counts['F']}")
print()

# Individual student results
print("INDIVIDUAL STUDENT RESULTS:")
print("-" * 40)
for i in range(len(student_names)):  # Proper indexing - no off-by-one error
    name = student_names[i]
    score = student_scores[i]
    
    # Determine letter grade
    if score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    
    # Show if above or below average
    comparison = "above average" if score > average_score else "below average" if score < average_score else "average"
    
    print(f"{name}: {score:.1f}% ({letter}) - {comparison}")

print("\nThank you for using Grade Tracker!")