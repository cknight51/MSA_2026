def main():
    a = -5
    b = 5

    if a > b:
       print(f"a = {a} is greater than b = {b}.")
    elif b > a:
        print(f"b = {b} is greater than a = {a}.")
    else:
        print(f"a = {a} is equal to b = {b}.")

    c = 4
    d = 10

    if a==4 or b== 5 or c == 5 or d == 9:
        print("The OR condition is True")
    else:
        print("The OR condition is False")

    # Print the appropriate letter grade base on a test score
    # A: 100 - 90, B: 89 - 80, C: 79-70, D: 69 - 60, F: less than 60
    # test_score = 83:
    # Output: 83% --> B
    print("\nGrade Decision: 1\n-------------")
    while True:
        try:
            test_score = float(input("Enter grade: "))
            if test_score < 0:
                print("ERROR: Please enter a grade of at least 0.")
                continue
            break
        except:
            print("ERROR: Please enter a number.")
            continue

    if test_score >= 90:
        print(f"{test_score}% --> A")
    elif test_score >= 80:
        print(f"{test_score}% --> B")
    elif test_score >= 70:
        print(f"{test_score}% --> C")
    elif test_score >= 60:
        print(f"{test_score}% --> D")
    else:
        print(f"{test_score}% --> F")

main()
