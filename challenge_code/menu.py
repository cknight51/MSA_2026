def main():
    total = 0
    while True:
        menu = {
            "Baja Taco" : 4.00,
            "Burrito" : 7.50,
            "Bowl" : 8.50,
            "Nachos" : 11.00,
            "Quesadilla" : 8.50,
            "Super Burrito" : 8.50,
            "Super Quesadilla" : 9.50,
            "Taco" : 3.00,
            "Tortilla Salad" : 8.00
        }
        
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