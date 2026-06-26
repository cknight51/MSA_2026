from Student import Student
from datetime import datetime

'''
Function to write an error message to a log file
Input: (str) Error message
Output: None
'''
def write_to_error_log(message: str) -> None:
    date = datetime.now()
    # Open the log file in append mode
    with open("error_log.txt", "a") as log_file:
        # Write an error message to the file
        log_file.write(f"{date}: {message}\n")

'''
Function to return a list of student objects
Input: None
Output: List of student objects
'''
def load_students() -> list[Student]:
    # Open students.csv
    data_file = open("students.csv")
    
    # Create an empty list of students
    students = []

    # Iterate of each line of students.csv and split on commas
    line_number = 0
    for line in data_file:
        # Skip the header line
        line_number += 1
        if line_number == 1:
            continue

        # Split the line of data and make a list of student data
        student_data = line.split(",")

        # Check if the list has the proper amount of items
        if len(student_data) != 6:
            write_to_error_log(f"ERROR: Invalid formatting on Line {line_number} of the file. Data has {len(student_data)} items but should have 6.")
            continue
        
        # Try to make a Student, if failed, print error statement 
        try:
            student: Student = Student(student_data[0], student_data[1], student_data[2], int(student_data[3]), float(student_data[4]), student_data[5])
        except:
            write_to_error_log(f"ERROR: Invalid formatting on Line {line_number} of the file. Credit hours or GPA are invalid values.")
            continue

        # Add student to the list of students
        students.append(student)

    data_file.close()
    return students

'''
Function to convert student objects into student dictinoaries
Input: List of student objects
Output: List of student dictionaries
'''
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    # Create an empty list to store the dictionaries
    student_dictionary_list = []

    # Loop through list_of_students and write each student's data to a dictionary
    for student in list_of_students:
        # Create an empty dictionary
        student_dictionary = {}

        # Make entries into the dictionary using the student properties
        # firstname, lastname, major, gpa, class, id
        student_dictionary["first_name"] = student.get_first_name()
        student_dictionary["last_name"] = student.get_last_name()
        student_dictionary["major"] = student.get_major()
        student_dictionary["gpa"] = student.get_gpa()
        student_dictionary["class"] = student.get_class_level()
        student_dictionary["id"] = student.get_id().strip()

        # append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)

    # return the list of dictionaries
    return student_dictionary_list

'''
Function to get student dictionaries
Input: None
Output: List of student dictionaries
'''
def get_student_dicitonaries():
    # Get a list of students
    student_list = load_students()

    # Get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)
    
    # Return a list of student dictionaries
    return student_dictionaries
