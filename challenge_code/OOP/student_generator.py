from Student import Student

def main():
    # Open students.csv
    data_file = open("students.csv")
    
    # Create an empty list of students
    students = []

    # Iterate of each line of students.csv and split on commas
    line_count = -1
    for line in data_file:
        line_count += 1
        if line_count == 0:
            continue
        student_data = line.split(",")
        if len(student_data) != 6:
            print(f"ERROR: Invalid formatting: {line}")
            continue
        try:
            student: Student = Student(student_data[0], student_data[1], student_data[2], int(student_data[3]), student_data[4], student_data[5])
        except:
            print(f"ERROR: {student_data[3]} is not a valid number of credit hours")
            continue

        students.append(student)
    
    for student in students:
        student.print_student_data()

main()
