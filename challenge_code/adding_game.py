import random

def get_difficulty():
    while True:
        try:
            difficulty = int(input("Enter Level (1, 2, 3): "))
            if difficulty in range (1, 4):
                return difficulty
            print("ERROR: Invalid input!")
        except:
            print("ERROR: Invalid input!")

def get_num_of_questions():
    while True:
        try: 
            num_of_questions = int(input("Enter number of questions to ask (3-10): "))
            if num_of_questions in range (3, 11):
                return num_of_questions
            print("ERROR: Please enter an integer value between 3 and 10!")
        except:
            print("ERROR: Please enter an integer value between 3 and 10!")

def main():
    difficulty = get_difficulty()
    if difficulty == 1:
        num_min = 0
        num_max = 9
    elif difficulty == 2:
        num_min = 10
        num_max = 99
    else:
        num_min = 100
        num_max = 999
    
    questions = get_num_of_questions()
    correct = 0

    for _ in range(questions):
        num_1 = random.Random().randint(num_min, num_max)
        num_2 = random.Random().randint(num_min, num_max)
        attempting = True
        attempts = 0
        while attempting and attempts < 3:
            answer = input(f"{num_1} + {num_2} = ")
            if answer == str(num_1 + num_2):
                print("CORRECT!!!")
                correct += 1
                attempting = False
            else:
                print("WRONG!!!")
                attempts += 1
        if attempting > 2:
            print(f"Correct Answer: {num_1} + {num_2} = {num_1 + num_2}")

    print(f"You got {correct} out of {questions} correct: {100 * (correct / questions):.2f}%")

main()