# Quiz Scorer - 15 Minute Mini Project
# Covers: print(), input(), for loops, bounds, augmented assignment

print("=== QUIZ SCORER ===")
print("This program will score a True/False quiz.")
print()

# Get basic information
student_name = input("Enter student name: ")
num_questions = int(input("How many questions on the quiz? (1-10): "))
print(f"\nScoring quiz for {student_name} with {num_questions} questions.")
print()

# Collect student answers using for loop with proper bounds
print("Enter student's answers (1 for True, 0 for False):")
student_answers = []

# KEY CONCEPT: range(1, n+1) for human-readable numbering (avoids off-by-one)
for question_num in range(1, num_questions + 1):
    print(f"Question {question_num}: ", end="")
    answer = int(input())
    student_answers.append(answer)

print()

# Collect correct answers using same loop structure
print("Enter correct answers (1 for True, 0 for False):")
correct_answers = []

for question_num in range(1, num_questions + 1):  # Same bounds as above
    print(f"Question {question_num} correct answer: ", end="")
    answer = int(input())
    correct_answers.append(answer)

# Score the quiz using augmented assignment
correct_count = 0  # Initialize counter

# KEY CONCEPT: range(len()) for list indexing (0 to len-1, no off-by-one)
print("\nGrading quiz...")
for i in range(len(student_answers)):
    if student_answers[i] == correct_answers[i]:
        correct_count += 1  # AUGMENTED ASSIGNMENT: same as correct_count = correct_count + 1
        print(f"✓ Question {i + 1}: Correct")
    else:
        print(f"✗ Question {i + 1}: Wrong")

# Calculate final results
percentage = (correct_count / num_questions) * 100

# Determine pass/fail
status = "PASS" if percentage >= 70 else "FAIL"

# Display formatted results
print("\n" + "=" * 40)
print(f"QUIZ RESULTS FOR {student_name.upper()}")
print("=" * 40)
print(f"Correct Answers: {correct_count}/{num_questions}")
print(f"Quiz Percentage: {percentage:.1f}%")
print(f"Final Status: {status}")
print("=" * 40)

# Bonus: Show which questions were missed (demonstrates more loop concepts)
if correct_count < num_questions:
    print("\nQuestions missed:")
    missed_count = 0  # Another variable for augmented assignment
    for i in range(len(student_answers)):  # Same indexing pattern
        if student_answers[i] != correct_answers[i]:
            missed_count += 1  # Count missed questions
            print(f"  Question {i + 1}: Student answered {student_answers[i]}, correct answer was {correct_answers[i]}")
    print(f"Total missed: {missed_count}")

print("\nThank you for using Quiz Scorer!")