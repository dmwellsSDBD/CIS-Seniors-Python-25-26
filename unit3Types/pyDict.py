'''
Student Grade Book Manager

Program: pyDict.py
Author: David Wells
Date: 11/04/2025

- Student ID: "S12345"
- Grade Level: 12
- Email: "emma.r@school.edu"
- Math grade: 95
- English grade: 88
- Science grade: 92
- Homework Completed: True

Tasks:
1. Create a dictionary called student1 with all the information above
2. Print the entire dictionary
3. Print just Emma's email address
4. Print just Emma's math grade
'''

# Part 1: Create your dictionary here
student1 = {
    "name": "Emma Rodriguez",
    "student_id": "S12345",
    "grade_level": 12,
    "email": "emma.r@school.edu",
    "math_grade": 95,
    "english_grade": 88,
    "science_grade": 92,
    "homework_completed": True
}

# Print the entire dictionary
print("Complete student record:")
print(student1)

# Print specific values
print("\nStudent email:", student1["email"])
print("Math grade:", student1["math_grade"])

# Part 2

# Modify Emma's homework status
student1["homework_completed"] = False

# Update her English grade
student1["english_grade"] = 91

# Add a history grade
student1["history_grade"] = 89

# Add clubs information
student1["clubs"] = ["Debate Team", "Math Club"]

# Print the updated dictionary
print("\nUpdated student record:")
print(student1)

# Part 3: Create a function to calculate average grade
# Python function structure: def (keyword) func_name(arguments)
def calculate_average(student): 
    '''
    this function calculates the students average
    '''
    # Get all the grades
    math = student1["math_grade"]
    english = student1["english_grade"]
    science = student1["science_grade"]
    history = student1["history_grade"]

    # Calculate average
    total = math + english + science + history
    average = total / 4

    # Return the average
    return average

# Test your function
# function call:
average = calculate_average(student1)
print(f"\n{student1['name']}'s average grade: {average:.2f}")


# Part 4: Using Dictionary Methods
# 1. Print all keys
print("\nAll keys in the dictionary:")
print(student1.keys())

# 2. Print all values
print("\nAll values in the dictionary:")
print(student1.values())


# 3. Print all key-value pairs
print("\nAll the key-value pairs:")
# print(student1.items())
for key, value in student1.items():
    print(f"{key}: {value}")


#4. Safely get phone number (doesn't exist)
# phone = 
# print("\nPhone number:", phone)
student1.get("phone_number")

phone = student1.get("phone_number", "Not Available")
student1.get("phone_number")


#5 Create new student and use update()
student2 = {
    "name": "Marcus Chen",
    "student_id": "S12346"
}

# Use . update() to add these fields all at once:
# grade_level: 11, math_grade: 87, english_grade 90, science_grade: 85
# more_info = {}
# student2.update(more_info)
student2.update({
    "grade_level": 11,
    "math_grade": 87,
    "english_grade": 90, 
    "science_grade": 85
})


print("\nNew student record:")
print(student2)