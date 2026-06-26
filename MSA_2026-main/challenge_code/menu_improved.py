def load_menu(file:str) -> dict:
    # Open menu.txt: Create a file handler to open a file in read mode
    data_file = open(file)
    print(data_file)

    # Create an empty dictionary
    menu = {}

    # Use a loop to read the contents of the file line by line
    for line in data_file:
        # Split the line at the comma
        item_and_price = line.split(",")
        # Get the item and price from the list
        item = item_and_price[0]
        price = float(item_and_price[1])
        # Create an entry in the dictionary for the item and price
        menu[item] = price

    # Close the file
    data_file.close()

    # Return the menu dictionary
    return menu

def main():
    total = 0
    while True:
        # Retrieve the menu dictionary 
        menu = load_menu("challenge_code\menu.txt")
        
        # Prompt the user to enter a menu item and convert it into title case with the title() method
        item = input("Item: ").title()

        # If the user enters "end" in any case, end the program
        if item == "End":
            break

        # Check if the entered item is not in the menu dictionary, if True, reprompt the user
        if item not in menu.keys():
            continue

        # Add the price of the item to a variable that stores the running total
        total += menu[item]

        # Print the running total to the user
        print(f"Total: ${total:,.2f}")

main()