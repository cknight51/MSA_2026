def main():
    while True:
        # INPUT
        # Prompt the user to enter the expression until valid
        expression = input("Expression: ")
        
        # Validate the following:
        # Check if the user properly separated the values and operator with spaces
        data = expression.split(" ")
        if len(data) != 3:
            print("ERROR: Incorrect format")
            continue
        
        # Try converting X and Z to integers, and if either conversion causes an exception, print integer error
        try:
            x = int(data[0])
            z = int(data[2])
        except:
            print("ERROR: X and Z must be integers")
            continue

        # Make a set of operators to determine if Y is a valid operator, if it is invalid, print operator error
        y = data[1]
        valid_operators = {"+", "-", "*", "/"}
        if y not in valid_operators:
            print("ERROR: Y must be a valid operator (+, -, *, /)")
            continue
        
        # PROCESS
        # Check which operator is being used and convert the expression from a list into a math function
        if y == "+":
            # Add X to Z to find the result
            result = float(x + z)
        elif y == "-":
            # Subtract Z from X to find the result
            result = float(x - z)
        elif y == "*":
            # Multiply X by Z to find the result
            result = float(x * z)
        else:
            # Check if the user divided by 0, if so, print divide by 0 error
            if z == 0:
                print("ERROR: Cannot divide by 0")
                continue
            # Divide X by Z to find to result
            result = float(x / z)

        # Print the output to the user rounded to 1 decimal place
        print(f"{result:.1f}")

        # Prompt the user to enter a new expression
        if input("Would you like to enter a new expression (enter 'y' to continue): ").lower() != "y":
            break

main()
