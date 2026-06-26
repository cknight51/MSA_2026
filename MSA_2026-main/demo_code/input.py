# Program to convert lbs to kg

# INPUT (getting the data that will be processed)
# Prompt user to enter weight in lbs
user_weight = float(input("Enter weight in lbs: "))

# PROCESSING
# Use a conversion factor to convert lbs to kg (2.205 lbs = 1 kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg

# OUTPUT
# Print the output to the user
print(f"You weigh {user_weight_in_kg:.2f} kg.")