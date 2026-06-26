# Print Hello world
print("Hello, World!")

# Create a variable to store my first name
first_name = "Collin"

# Create a variable to store my last name
last_name = "Knight"

# Write a python statement to display "My full name is first_name last_name"
print("My full name is", first_name, last_name)

# Print using the f string (string interpolation)
print(f"My full name is {first_name} {last_name}.")

# Create variables to store age and weight
age = 16
weight = 138.6
half_age = age / 2

# Print a sentence with name, age, and weight
print(f"\nMy name is {first_name} {last_name}.\nI am {age} years old and I weigh {weight} lbs.")

# Get and print the data type for age, weight, and half_age
print("\nChecking data types\n-------------------")
print(type(age))
print(type(weight))
print(type(half_age))

# Write 3 statements using string interpolation (f string) to print descriptive sentences for the data types
print(f"Variable age is an {type(age)}.")
print(f"Variable weight is a {type(weight)}.")
print(f"Variable half_age is a {type(half_age)}.")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")