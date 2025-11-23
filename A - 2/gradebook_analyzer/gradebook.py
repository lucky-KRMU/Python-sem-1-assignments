"""
GradeBook Analyzer CLI
Author: Lucky Pawar
Date: November 23, 2025
Title: Analysing and Reporting Student Grades

Description:
A command-line tool to read student marks (manual or CSV),
perform statistical analysis, assign letter grades, and generate a summary report.
"""
import statistics
import csv
from typing import Dict, List, Tuple

# --- Task 3: Statistical Analysis Functions ---
def calculate_average(marks_dict: Dict[str, int]) -> float:
    """Calculates the mean (average) of all marks."""
    if not marks_dict:
        return 0.0
    # The statistics module is used for reliable calculation
    return statistics.mean(marks_dict.values())
    
def calculate_median(marks_dict: Dict[str, int]) -> float:
    """Calculates the median of all marks."""
    if not marks_dict:
        return 0.0
    # Sort the list of marks to find the median
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict: Dict[str, int]) -> int:
    """Finds the maximum score."""
    return max(marks_dict.values()) if marks_dict else 0

def find_min_score(marks_dict: Dict[str, int]) -> int:
    """Finds the minimum score."""
    return min(marks_dict.values()) if marks_dict else 0

# --- Task 4: Grade Assignment and Distribution ---
def assign_grade(score: int) -> str:
    """Assigns a letter grade based on the score."""
    # Grading scheme: A: 90+, B: 80–89, C: 70–79, D: 60–69, F: <60 
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def generate_grades(marks_dict: Dict[str, int]) -> Tuple[Dict[str, str], Dict[str, int]]:
    """
    Generates a dictionary of grades and counts the distribution.
    
    """
    grades_dict = {}
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for name, score in marks_dict.items():
        grade = assign_grade(score)
        grades_dict[name] = grade
        grade_counts[grade] += 1
        
    return grades_dict, grade_counts

# --- Task 2: Data Entry or CSV Import ---
def manual_input() -> Dict[str, int]:
    """Allows manual entry of student names and marks."""
    print("\n--- Manual Data Entry ---")
    marks = {}
    while True:
        try:
            name = input("Enter student name (or 'done' to finish): ").strip()
            if name.lower() == 'done':
                break
            
            # Input validation for mark
            mark_input = input(f"Enter mark for {name} (0-100): ").strip()
            mark = int(mark_input)
            
            if 0 <= mark <= 100:
                marks[name] = mark
            else:
                print("Mark must be between 0 and 100. Please try again.")
                
        except ValueError:
            print("Invalid input for mark. Please enter a whole number.")
            
    return marks

def load_csv(file_path: str) -> Dict[str, int]:
    """Loads student names and marks from a CSV file."""
    marks = {}
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            # Optional: Skip header row if it exists
            # next(reader) 
            
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip()
                    try:
                        # Assuming name is in column 1, mark in column 2
                        mark = int(row[1].strip())
                        if 0 <= mark <= 100:
                            marks[name] = mark
                        else:
                            print(f"Warning: Skipping {name} due to invalid mark ({mark}).")
                    except ValueError:
                        print(f"Warning: Skipping row for {name} due to non-numeric mark.")
                else:
                    print(f"Warning: Skipping incomplete row: {row}")

    except FileNotFoundError:
        print(f"\nError: File not found at {file_path}")
    except Exception as e:
        print(f"\nAn error occurred while reading the CSV file: {e}")
        
    return marks

def get_data_from_user() -> Dict[str, int]:
    """Prompts the user for the data input method."""
    print("\nSelect input method:")
    print("1: Manual entry of student names and marks")
    print("2: Load from a .csv file")
    
    while True:
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == '1':
            return manual_input()
        elif choice == '2':
            file_path = input("Enter the path to the CSV file (e.g., marks.csv): ").strip()
            return load_csv(file_path)
        else:
            print("Invalid choice. Please enter 1 or 2.")

# --- Analysis and Reporting ---
def generate_summary(marks_dict: Dict[str, int], grades_dict: Dict[str, str], grade_counts: Dict[str, int]):
    """Prints the statistical analysis and grade distribution summary."""
    num_students = len(marks_dict)
    if num_students == 0:
        print("\nNo student data to analyze.")
        return

    # Task 3: Display Statistical Summary 
    print("\n" + "="*40)
    print("      *** Statistical Summary ***")
    print("="*40)
    print(f"Total Students: {num_students}")
    print(f"Average Score:  {calculate_average(marks_dict):.2f}")
    print(f"Median Score:   {calculate_median(marks_dict):.1f}")
    print(f"Maximum Score:  {find_max_score(marks_dict)}")
    print(f"Minimum Score:  {find_min_score(marks_dict)}")
    print("="*40)
    
    # Task 4: Display Grade Distribution 
    print("\n" + "-"*35)
    print("      *** Grade Distribution ***")
    print("-" * 35)
    total_counted = sum(grade_counts.values())
    for grade, count in grade_counts.items():
        percentage = (count / total_counted) * 100 if total_counted > 0 else 0
        print(f"Grade {grade}: {count} students ({percentage:.1f}%)")
    print("-" * 35)

    # Task 5: Pass/Fail Filter with List Comprehension 
    # Assuming Pass mark is >= 40 for this example
    pass_mark = 40
    
    # List comprehension to filter passed students
    passed_students = [
        name for name, mark in marks_dict.items() if mark >= pass_mark
    ]
    # List comprehension to filter failed students
    failed_students = [
        name for name, mark in marks_dict.items() if mark < pass_mark
    ]
    
    print("\n" + "*" * 35)
    print("      *** Pass/Fail Summary ***")
    print("*" * 35)
    print(f"Total Passed (>= {pass_mark}): {len(passed_students)}")
    print(f"Total Failed (< {pass_mark}):  {len(failed_students)}")
    
    print("\nFailed Students:")
    print(", ".join(failed_students) if failed_students else "None")
    print("*" * 35)

# --- Task 6: Results Table and User Loop ---
def print_results_table(marks_dict: Dict[str, int], grades_dict: Dict[str, str]):
    """Prints the final results in a formatted table. """
    if not marks_dict:
        return
    
    # Header formatting
    header = f"{'Name':<15}{'Marks':<10}{'Grade':<5}"
    separator = "-" * len(header)
    
    print("\n" + "=" * 30)
    print("       *** Final Gradebook ***")
    print("=" * 30)
    print(header)
    print(separator)
    
    # Data rows - sort by name for consistent output
    for name in sorted(marks_dict.keys()):
        mark = marks_dict[name]
        grade = grades_dict.get(name, "N/A") # Use .get for safety
        
        # Use f-strings for clean formatting 
        print(f"{name:<15}{mark:<10}{grade:<5}")
        
    print(separator)

def main_cli_loop():
    """The main command-line interface loop for repeated analysis. """
    print("="*50)
    print("  Welcome to the Python GradeBook Analyzer CLI! ")
    print("="*50)

    while True:
        # Get data from user
        marks_data = get_data_from_user()
        
        if marks_data:
            # 1. Generate Grades
            grades_data, distribution = generate_grades(marks_data)

            # 2. Generate Summary Report
            generate_summary(marks_data, grades_data, distribution)
            
            # 3. Print Final Results Table
            print_results_table(marks_data, grades_data)

        # Allow user to repeat analysis or exit program 
        print("\nWhat would you like to do next?")
        print("1: Analyze another set of grades")
        print("2: Exit the program")
        
        repeat_choice = input("Enter choice (1 or 2): ").strip()
        
        if repeat_choice == '2':
            print("\nThank you for using the GradeBook Analyzer. Goodbye!")
            break
        elif repeat_choice != '1':
            print("Invalid choice. Continuing analysis...")

# Entry point of the script
if __name__ == "__main__":
    main_cli_loop()