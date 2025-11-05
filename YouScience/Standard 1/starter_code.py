"""
Student Grade Management System - STARTER TEMPLATE
YOUR NAME: ___________________________
DATE: ___________________________

Complete this program to demonstrate your mastery of:
- Static Arrays (Objective 1)
- Dynamic Lists (Objective 2)
- String Operations (Objective 3)
"""

# ============================================
# PART 1: STATIC ARRAY OPERATIONS
# ============================================

def create_score_array():
    """
    TODO: Create and return a fixed-size list of 5 test scores
    Initialize all values to 0.0
    """
    # Your code here
    pass


def input_scores(scores):
    """
    TODO: Get 5 test scores from user (0-100)
    Store them in the scores array
    Include error checking
    """
    # Your code here
    pass


def output_scores(scores):
    """
    TODO: Display all test scores
    Use a for-each loop to iterate
    """
    # Your code here
    pass


def sort_scores(scores):
    """
    TODO: Sort the scores from highest to lowest
    Return the sorted array
    """
    # Your code here
    pass


def calculate_statistics(scores):
    """
    TODO: Calculate average, highest, and lowest scores
    Use a for loop to iterate through scores
    Return a dictionary with the results
    """
    # Your code here
    pass


# ============================================
# PART 2: DYNAMIC LIST OPERATIONS
# ============================================

class Student:
    """Student record class"""
    def __init__(self, full_name, student_id):
        # TODO: Initialize student attributes
        pass
    
    def calculate_average(self):
        # TODO: Calculate student's average grade
        pass
    
    def get_letter_grade(self):
        # TODO: Convert average to letter grade
        pass


def create_student_list():
    """
    TODO: Create and return an empty dynamic list
    """
    # Your code here
    pass


def add_student(students, full_name, student_id):
    """
    TODO: Create new student and add to dynamic list
    """
    # Your code here
    pass


def remove_student(students, search_name):
    """
    TODO: Remove student from list by name
    Use string comparison to find student
    """
    # Your code here
    pass


def display_all_students(students):
    """
    TODO: Display all students using for-each loop
    Show formatted output with name, ID, and average
    """
    # Your code here
    pass


def sort_students_by_name(students):
    """
    TODO: Sort students alphabetically by name
    """
    # Your code here
    pass


# ============================================
# PART 3: STRING OPERATIONS
# ============================================

def compare_strings(str1, str2):
    """
    TODO: Compare two strings
    Return exact match and case-insensitive match results
    """
    # Your code here
    pass


def get_string_length(text):
    """
    TODO: Return the length of a string
    Check if length is at least 3 characters
    """
    # Your code here
    pass


def extract_name_parts(full_name):
    """
    TODO: Extract first name and last name from full name
    Return both parts in a dictionary
    """
    # Your code here
    pass


def concatenate_student_info(first_name, last_name, student_id, grade):
    """
    TODO: Concatenate strings to create formatted output
    Format: "Last, First (ID: xxxxx) - Grade: X"
    """
    # Your code here
    pass


def find_substring_position(text, substring):
    """
    TODO: Find position of substring in text
    Return position and whether it was found
    """
    # Your code here
    pass


def create_student_initials(full_name):
    """
    TODO: Create initials from full name
    Example: "John Smith" -> "JS"
    """
    # Your code here
    pass


def format_student_name(full_name, format_type):
    """
    TODO: Format name in different styles
    Styles: "last_first", "first_last", "formal", "initials"
    """
    # Your code here
    pass


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """
    TODO: Create main program with menu system
    Include options to:
    - Add students
    - Remove students
    - Enter test scores
    - Display students
    - Sort students
    - Search for students
    """
    # Your code here
    pass


if __name__ == "__main__":
    main()