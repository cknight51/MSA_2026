# Functions to convert lbs to kg

def get_positive_float_input():
    # Loop
    while True:
        # Validate input (ensure the data is a numeric value)
        try: 
            # Prompt user to enter weight in lbs
            user_weight = float(input("Enter weight in lbs: "))
            # If user_weight is less or equal than 0, output error message and reprompt the user
            if user_weight <= 0:
                print("ERROR: Enter a number greater than 0.\n")
                continue
            return user_weight
        except:
            # If input is invalid, then reprompt the user until the input is valid
            print("ERROR: Please enter a number.\n")
            continue
        
    
def main():
    # INPUT (getting the data that will be processed)
    user_weight = get_positive_float_input()
    
    # PROCESSING
    # Use a conversion factor to convert lbs to kg (2.205 lbs = 1 kg)
    lbs_to_kg = 2.205
    user_weight_in_kg = user_weight / lbs_to_kg

    # OUTPUT
    # Print the output to the user
    print(f"You weigh {user_weight_in_kg:.2f} kg.")

main()