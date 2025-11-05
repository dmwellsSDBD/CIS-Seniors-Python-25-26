"""
Student Grade Management System
YouScience Computer Programming 2 - Standard 1 Project
Demonstrates: Static Arrays, Dynamic Lists, and String Operations
"""

# ============================================
# PART 1: STATIC ARRAY OPERATIONS
# ============================================

def create_score_array():
    """
    Objective 1.1: Declare and initialize arrays of all applicable types
    Creates a fixed-size array of 5 test scores
    """
    scores = [0.0, 0.0, 0.0, 0.0, 0.0]  # Static array of 5 floats
    return scores


def input_scores(scores):
    """
    Objective 1.2: Perform data input to arrays
    Gets test scores from user and stores in array
    """
    print("\nEnter 5 test scores (0-100):")
    for i in range(len(scores)):
        while True:
            try:
                score = float(input(f"  Test {i+1}: "))
                if 0 <= score <= 100:
                    scores[i] = score
                    break
                else:
                    print("  Error: Score must be between 0 and 100")
            except ValueError:
                print("  Error: Please enter a valid number")
    return scores


def output_scores(scores):
    """
    Objective 1.2: Perform data output from arrays
    Objective 1.4: Iterate through structure using for-each
    """
    print("\nTest Scores:")
    test_num = 1
    for score in scores:  # For-each iteration
        print(f"  Test {test_num}: {score:.1f}")
        test_num += 1


def sort_scores(scores):
    """
    Objective 1.3: Perform operations on arrays including sort
    Returns sorted copy of scores (highest to lowest)
    """
    sorted_scores = scores.copy()
    sorted_scores.sort(reverse=True)
    return sorted_scores


def calculate_statistics(scores):
    """
    Objective 1.3: Perform operations on arrays
    Objective 1.4: Iterate through structure
    """
    total = 0.0
    highest = scores[0]
    lowest = scores[0]
    
    # Use standard for loop to iterate and calculate
    for i in range(len(scores)):
        total += scores[i]
        if scores[i] > highest:
            highest = scores[i]
        if scores[i] < lowest:
            lowest = scores[i]
    
    average = total / len(scores)
    
    return {
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'total': total
    }


# ============================================
# PART 2: DYNAMIC LIST OPERATIONS
# ============================================

class Student:
    """
    Student record class to store in dynamic list
    """
    def __init__(self, full_name, student_id):
        self.full_name = full_name
        self.student_id = student_id
        self.test_scores = create_score_array()
        self.average = 0.0
    
    def calculate_average(self):
        """Calculate and update student's average"""
        stats = calculate_statistics(self.test_scores)
        self.average = stats['average']
        return self.average
    
    def get_letter_grade(self):
        """Convert numeric average to letter grade"""
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'


def create_student_list():
    """
    Objective 2.1: Declare and initialize a dynamic array/list
    Creates empty dynamic list for student records
    """
    students = []  # Dynamic list initialization
    return students


def add_student(students, full_name, student_id):
    """
    Objective 2.2: Add items to the array/list
    Adds new student to dynamic list
    """
    new_student = Student(full_name, student_id)
    students.append(new_student)  # Dynamic addition
    print(f"✓ Added student: {full_name}")
    return students


def remove_student(students, search_name):
    """
    Objective 2.2: Remove items from the array/list
    Objective 3.1: Compare string values
    """
    for i in range(len(students)):
        # String comparison to find student
        if students[i].full_name.lower() == search_name.lower():
            removed = students.pop(i)  # Dynamic removal
            print(f"✓ Removed student: {removed.full_name}")
            return True
    print(f"✗ Student not found: {search_name}")
    return False


def display_all_students(students):
    """
    Objective 2.3: Output data from arrays/lists
    Objective 2.5: Iterate through structure (for-each)
    """
    if len(students) == 0:
        print("\nNo students in the system.")
        return
    
    print("\n" + "="*70)
    print("STUDENT ROSTER")
    print("="*70)
    
    # For-each iteration through dynamic list
    for student in students:
        print(f"Name: {student.full_name:30s} ID: {student.student_id:10s} Avg: {student.average:.1f} ({student.get_letter_grade()})")
    
    print("="*70)
    print(f"Total Students: {len(students)}")


def sort_students_by_name(students):
    """
    Objective 2.4: Perform operations on arrays/lists
    Sorts dynamic list alphabetically by name
    """
    students.sort(key=lambda s: s.full_name.lower())
    print("✓ Students sorted alphabetically")


def sort_students_by_average(students):
    """
    Objective 2.4: Perform operations on arrays/lists
    Sorts dynamic list by grade average (highest first)
    """
    students.sort(key=lambda s: s.average, reverse=True)
    print("✓ Students sorted by grade average")


def count_students(students):
    """
    Objective 2.6: Use a loop to iterate through the structure
    Counts students using while loop iteration
    """
    count = 0
    i = 0
    while i < len(students):  # While loop iteration
        count += 1
        i += 1
    return count


def calculate_class_statistics(students):
    """
    Objective 2.6: Use a loop to iterate through structure
    Calculates class-wide statistics using for loop
    """
    if len(students) == 0:
        return None
    
    total_average = 0.0
    highest_avg = students[0].average
    lowest_avg = students[0].average
    
    # For loop iteration
    for i in range(len(students)):
        total_average += students[i].average
        if students[i].average > highest_avg:
            highest_avg = students[i].average
        if students[i].average < lowest_avg:
            lowest_avg = students[i].average
    
    class_average = total_average / len(students)
    
    return {
        'class_average': class_average,
        'highest_average': highest_avg,
        'lowest_average': lowest_avg
    }


# ============================================
# PART 3: STRING OPERATIONS
# ============================================

def compare_strings(str1, str2):
    """
    Objective 3.1: Compare string values
    Demonstrates multiple string comparison methods
    """
    exact_match = (str1 == str2)
    case_insensitive = (str1.lower() == str2.lower())
    
    return {
        'exact': exact_match,
        'case_insensitive': case_insensitive
    }


def get_string_length(text):
    """
    Objective 3.2: Find the length of a string
    Returns string length and validates minimum length
    """
    length = len(text)
    is_valid = length >= 3  # Minimum 3 characters for names
    
    return {
        'length': length,
        'is_valid': is_valid
    }


def extract_name_parts(full_name):
    """
    Objective 3.3: Copy part or all of string values into other strings
    Extracts first name, last name, and middle name if present
    """
    name_parts = full_name.strip().split()
    
    first_name = name_parts[0] if len(name_parts) > 0 else ""
    last_name = name_parts[-1] if len(name_parts) > 1 else ""
    middle_name = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""
    
    return {
        'first': first_name,
        'middle': middle_name,
        'last': last_name
    }


def concatenate_student_info(first_name, last_name, student_id, grade):
    """
    Objective 3.4: Concatenate string values
    Creates formatted student information string
    """
    # Multiple concatenation methods
    formatted_name = last_name + ", " + first_name
    full_info = formatted_name + " (ID: " + student_id + ") - Grade: " + grade
    
    return full_info


def find_substring_position(text, substring):
    """
    Objective 3.5: Locate substring positions
    Finds position of substring in text
    """
    position = text.find(substring)
    
    if position != -1:
        return {
            'found': True,
            'position': position,
            'message': f"'{substring}' found at position {position}"
        }
    else:
        return {
            'found': False,
            'position': -1,
            'message': f"'{substring}' not found"
        }


def insert_string_into_report(header, data, footer):
    """
    Objective 3.6: Insert strings into other strings
    Creates formatted report by inserting strings
    """
    # Build report by inserting strings at specific positions
    report = header + "\n"
    report += "-" * len(header) + "\n"
    report += data + "\n"
    report += "-" * len(header) + "\n"
    report += footer
    
    return report


def create_student_initials(full_name):
    """
    Objective 3.3 & 3.4: Extract and concatenate substrings
    Creates initials from full name
    """
    parts = extract_name_parts(full_name)
    
    initials = ""
    if parts['first']:
        initials += parts['first'][0].upper()
    if parts['middle']:
        initials += parts['middle'][0].upper()
    if parts['last']:
        initials += parts['last'][0].upper()
    
    return initials


def format_student_name(full_name, format_type):
    """
    Objective 3.3, 3.4, 3.6: Comprehensive string manipulation
    Formats name in different styles
    """
    parts = extract_name_parts(full_name)
    
    if format_type == "last_first":
        # Last, First format
        return parts['last'] + ", " + parts['first']
    elif format_type == "first_last":
        # First Last format
        return parts['first'] + " " + parts['last']
    elif format_type == "formal":
        # Mr./Ms. Last format
        return "Mr./Ms. " + parts['last']
    elif format_type == "initials":
        # Initials format
        return create_student_initials(full_name)
    else:
        return full_name


def validate_student_name(name):
    """
    Objective 3.2, 3.5: String length and substring checking
    Validates student name meets requirements
    """
    length_info = get_string_length(name)
    has_space = find_substring_position(name, " ")
    
    errors = []
    
    if not length_info['is_valid']:
        errors.append(f"Name too short (minimum 3 characters)")
    
    if not has_space['found']:
        errors.append("Name must include first and last name (with space)")
    
    if name != name.strip():
        errors.append("Name has leading/trailing spaces")
    
    is_valid = len(errors) == 0
    
    return {
        'valid': is_valid,
        'errors': errors,
        'length': length_info['length']
    }


def generate_student_report(student):
    """
    Comprehensive string operations for report generation
    Uses objectives 3.1-3.6
    """
    # Extract name parts (Objective 3.3)
    parts = extract_name_parts(student.full_name)
    
    # Create formatted name (Objective 3.4 - concatenation)
    formatted_name = format_student_name(student.full_name, "last_first")
    
    # Create initials (Objective 3.3, 3.4)
    initials = create_student_initials(student.full_name)
    
    # Get string length (Objective 3.2)
    name_length = len(student.full_name)
    
    # Build report header
    header = f"STUDENT GRADE REPORT - {initials}"
    
    # Build report data (Objective 3.4 - concatenation)
    data = f"Name: {formatted_name}\n"
    data += f"Student ID: {student.student_id}\n"
    data += f"Test Scores: "
    
    # Add scores (Objective 3.4)
    score_strings = [str(score) for score in student.test_scores]
    data += ", ".join(score_strings) + "\n"
    
    data += f"Average: {student.average:.2f}\n"
    data += f"Letter Grade: {student.get_letter_grade()}"
    
    # Create footer
    footer = f"Name Length: {name_length} characters"
    
    # Insert strings into report (Objective 3.6)
    report = insert_string_into_report(header, data, footer)
    
    return report


# ============================================
# MAIN PROGRAM / MENU SYSTEM
# ============================================

def display_menu():
    """Display main menu options"""
    print("\n" + "="*70)
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("="*70)
    print("1.  Add New Student")
    print("2.  Remove Student")
    print("3.  Enter Test Scores for Student")
    print("4.  Display All Students")
    print("5.  Display Individual Student Report")
    print("6.  Sort Students by Name")
    print("7.  Sort Students by Average Grade")
    print("8.  Display Class Statistics")
    print("9.  Search for Student")
    print("10. Demonstrate String Operations")
    print("0.  Exit Program")
    print("="*70)


def get_menu_choice():
    """Get valid menu choice from user"""
    while True:
        try:
            choice = int(input("\nEnter your choice (0-10): "))
            if 0 <= choice <= 10:
                return choice
            else:
                print("Error: Please enter a number between 0 and 10")
        except ValueError:
            print("Error: Please enter a valid number")


def find_student_by_name(students, search_name):
    """
    Search for student by name using string comparison
    Objective 3.1: Compare string values
    """
    for student in students:
        comparison = compare_strings(student.full_name, search_name)
        if comparison['case_insensitive']:
            return student
    return None


def demonstrate_string_operations():
    """
    Demonstrates all string operations (Objective 3)
    """
    print("\n" + "="*70)
    print("STRING OPERATIONS DEMONSTRATION")
    print("="*70)
    
    # Get test name
    test_name = input("\nEnter a full name to test: ")
    
    # Objective 3.2: String length
    length_info = get_string_length(test_name)
    print(f"\n1. STRING LENGTH:")
    print(f"   Length: {length_info['length']} characters")
    print(f"   Valid (3+ chars): {length_info['is_valid']}")
    
    # Objective 3.3: Extract substrings
    parts = extract_name_parts(test_name)
    print(f"\n2. EXTRACT NAME PARTS:")
    print(f"   First Name: '{parts['first']}'")
    print(f"   Middle Name: '{parts['middle']}'")
    print(f"   Last Name: '{parts['last']}'")
    
    # Objective 3.4: Concatenation
    if parts['first'] and parts['last']:
        concat_result = concatenate_student_info(
            parts['first'], 
            parts['last'], 
            "12345", 
            "A"
        )
        print(f"\n3. CONCATENATED STRING:")
        print(f"   {concat_result}")
    
    # Objective 3.5: Find substring
    search_substring = input("\n4. Enter a substring to search for: ")
    position_info = find_substring_position(test_name, search_substring)
    print(f"   {position_info['message']}")
    
    # Objective 3.6: String insertion (formatting)
    print(f"\n5. FORMATTED NAME VARIATIONS:")
    print(f"   Last, First: {format_student_name(test_name, 'last_first')}")
    print(f"   First Last: {format_student_name(test_name, 'first_last')}")
    print(f"   Formal: {format_student_name(test_name, 'formal')}")
    print(f"   Initials: {format_student_name(test_name, 'initials')}")
    
    # Objective 3.1: String comparison
    print(f"\n6. STRING COMPARISON:")
    compare_to = input("   Enter a name to compare to: ")
    comp_result = compare_strings(test_name, compare_to)
    print(f"   Exact match: {comp_result['exact']}")
    print(f"   Case-insensitive match: {comp_result['case_insensitive']}")
    
    # Validation
    validation = validate_student_name(test_name)
    print(f"\n7. NAME VALIDATION:")
    print(f"   Valid: {validation['valid']}")
    if not validation['valid']:
        print(f"   Errors: {', '.join(validation['errors'])}")


def main():
    """
    Main program loop - Grade Management System
    """
    # Initialize dynamic student list (Objective 2.1)
    students = create_student_list()
    
    # Add some sample students for testing
    print("Initializing system with sample data...")
    sample_students = [
        ("Sarah Johnson", "SJ2024001"),
        ("Michael Chen", "MC2024002"),
        ("Emily Rodriguez", "ER2024003")
    ]
    
    for name, student_id in sample_students:
        students = add_student(students, name, student_id)
    
    print(f"\n✓ System initialized with {len(students)} students")
    
    # Main program loop
    running = True
    while running:
        display_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            # Add new student
            print("\n--- ADD NEW STUDENT ---")
            full_name = input("Enter student's full name: ")
            
            # Validate name
            validation = validate_student_name(full_name)
            if not validation['valid']:
                print("✗ Invalid name:")
                for error in validation['errors']:
                    print(f"  - {error}")
                continue
            
            student_id = input("Enter student ID: ")
            students = add_student(students, full_name, student_id)
        
        elif choice == 2:
            # Remove student
            print("\n--- REMOVE STUDENT ---")
            search_name = input("Enter student name to remove: ")
            remove_student(students, search_name)
        
        elif choice == 3:
            # Enter test scores
            print("\n--- ENTER TEST SCORES ---")
            search_name = input("Enter student name: ")
            student = find_student_by_name(students, search_name)
            
            if student:
                print(f"\nEntering scores for: {student.full_name}")
                student.test_scores = input_scores(student.test_scores)
                student.calculate_average()
                print(f"✓ Scores entered. Average: {student.average:.2f}")
            else:
                print("✗ Student not found")
        
        elif choice == 4:
            # Display all students
            display_all_students(students)
        
        elif choice == 5:
            # Display individual report
            print("\n--- INDIVIDUAL STUDENT REPORT ---")
            search_name = input("Enter student name: ")
            student = find_student_by_name(students, search_name)
            
            if student:
                report = generate_student_report(student)
                print("\n" + report)
            else:
                print("✗ Student not found")
        
        elif choice == 6:
            # Sort by name
            sort_students_by_name(students)
            display_all_students(students)
        
        elif choice == 7:
            # Sort by average
            sort_students_by_average(students)
            display_all_students(students)
        
        elif choice == 8:
            # Class statistics
            stats = calculate_class_statistics(students)
            if stats:
                print("\n" + "="*70)
                print("CLASS STATISTICS")
                print("="*70)
                print(f"Total Students: {count_students(students)}")
                print(f"Class Average: {stats['class_average']:.2f}")
                print(f"Highest Average: {stats['highest_average']:.2f}")
                print(f"Lowest Average: {stats['lowest_average']:.2f}")
                print("="*70)
            else:
                print("\n✗ No students in system")
        
        elif choice == 9:
            # Search for student
            print("\n--- SEARCH FOR STUDENT ---")
            search_name = input("Enter student name: ")
            student = find_student_by_name(students, search_name)
            
            if student:
                print(f"\n✓ Found: {student.full_name}")
                print(f"  ID: {student.student_id}")
                print(f"  Average: {student.average:.2f}")
                print(f"  Grade: {student.get_letter_grade()}")
            else:
                print("✗ Student not found")
        
        elif choice == 10:
            # Demonstrate string operations
            demonstrate_string_operations()
        
        elif choice == 0:
            # Exit
            print("\n" + "="*70)
            print("Thank you for using the Student Grade Management System!")
            print("="*70)
            running = False
    
    # Final report
    print(f"\nFinal Statistics:")
    print(f"  Total students processed: {count_students(students)}")
    if len(students) > 0:
        stats = calculate_class_statistics(students)
        print(f"  Final class average: {stats['class_average']:.2f}")


# ============================================
# PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    main()