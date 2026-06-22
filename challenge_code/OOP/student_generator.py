from Student import Student

def main():
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
            print(f"ERROR: Invalid formatting on Line {line_number} of the file. Data has {len(student_data)} items but should have 6.\n")
            continue
            
        # Try to make a Student, if failed, print error statement 
        try:
            student: Student = Student(student_data[0], student_data[1], student_data[2], int(student_data[3]), float(student_data[4]), student_data[5])
        except:
            print(f"ERROR: Invalid formatting on Line {line_number}")
            continue

        # Add student to the list of students
        students.append(student)

    # Print each student's data
    for student in students:
        student.print_student_data()

main()
