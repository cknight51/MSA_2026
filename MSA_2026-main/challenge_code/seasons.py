''' Create a decision structure to determine the season:
Winter, spring, summer, fall
Prompt the user to enter the number of the month. Month must be from 1 to 12
Winter = 12, 1, | Spring = 3, 4, 5 | Summer = 6, 7, 8 | Fall = 9, 10, 11
Output the season
"Enter month number: (11)"
Output: It is fall. '''

def main():
    # Loop until valid input
    while True:
        try:
            # Prompt the user for month number
            month = int(input("Enter month number (1-12): "))
            # Validate input
            if month in range(1,13):
                break
            # Print error message
            print("ERROR: Please enter an integer from 1 to 12")
        except:
            # Print error message
            print("ERROR: Please enter an integer from 1 to 12")

    # Check if the month is in winter
    if month == 12 or month in range(1,3):
        print("It is winter.")
    # Check if the month is in spring
    elif month in range (3,6):
        print("It is spring.")
    # Check if the month is in summer
    elif month in range(6,9):
        print("It is summer.")
    # Check if the month is in fall
    else:
        print("It is fall.")

main()