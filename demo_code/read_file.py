def main():
    # Open menu.txt: Create a file handler to open a file in read mode
    data_file = open("menu.txt")
    print(data_file)

    # Create an empty dictionary
    menu = {}

    # Use a loop to read the contents of the file line by line
    for line in data_file:
        # Split the line at the comma
        item_and_price = line.split(",")
        # Get the item and price from the list
        item = item_and_price[0]
        price = item_and_price[1]
        # Create an entry in the dictionary for the item and price
        menu[item] = price

    # Close the file


main()