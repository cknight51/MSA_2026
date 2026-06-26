def get_data(prompt, max):
    # Loop until a valid input
    while True:
        try:
            data = float(input(f"Enter the {prompt}: "))
            # Validate user input
            if 0 < data <= max:
                return data
            # Print error message 
            print("ERROR: Enter a number between 0 and 24.")
        except:
            # Print error message
            print("ERROR: Please enter a number.")

def main():
    # Get data from the user
    hours = get_data("number of hours worked daily", 24)
    wage = get_data("hourly wage", float("inf"))
    # Calculate Pay Advice
    gross_income = 350 * hours * wage
    taxes = .12 * gross_income
    net_income = gross_income - taxes

    # Output Pay Advice
    print("\nPay Advice\n-------------")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Wage: ${wage:,.2f}")
    print(f"Wages Before Taxes: ${gross_income:,.2f}")
    print(f"Tax Amount: ${taxes:,.2f}")
    print(f"Annual Wage After Taxes: ${net_income:,.2f}\n")

main()
