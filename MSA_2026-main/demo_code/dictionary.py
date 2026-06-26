def main():
    # The need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    # Print the names of the students with their scores
    print("\nStudents and Scores Using the Lists\n------------------------------------")
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")

    # Create a dictionary of names and scores
    student_scores = {
        "Alice" : 55,
        "Bob" : 75,
        "Jerry" : 87, 
        "Jane" : 82, 
        "Bill" : 91
    }

    # Print Bob and Jane's scores
    print("\nPrint Bob and Jane's Scores\n----------------------------")
    print(student_scores["Bob"])
    print(student_scores["Jane"])

    # Print all the data in the student_scores dictionary
    print("\nPrint All Student Data\n-----------------------")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

main()