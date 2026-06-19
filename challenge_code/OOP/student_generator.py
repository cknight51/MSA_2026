from Student import Student

def main():
    # Open students.csv
    data_file = open("challenge_code\OOP\students.csv")
    
    # Create an empty list of students
    students = []

    # Iterate of each line of students.csv and split on commas
    for line in range(1, len(data_file)):
        student_data = line.split(",")
        if len(student_data) != 6:
            print(f"ERROR: Invalid formatting on Line {line}")
            continue
        try:
            student = Student(student_data[0], student_data[1], student_data[2], int(student_data[3]), student_data[4], student_data[5])
        except:
            print(f"ERROR: {student_data[3]} is not a valid number of credit hours")
            continue
        





main()