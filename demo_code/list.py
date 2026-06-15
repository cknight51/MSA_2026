def main():
    # Create a list of strings, integers, and differing values
    names = ["John", "Mary", "Alice", "Bob"]
    integers = [10, 16, 24, 42, 14, 9]
    random = ["Cyd", 15, 22.3, True, "Frank"]
    empty = []

    # Print a list 
    print(integers)
    print(names)

    # Add values to a list
    print("\nAdding Values to a List\n-----------------------")
    names.append("Johnny")
    integers.append(63)
    integers.append(5)
    print(f"List of Integers: {integers}")
    print(f"List of Names: {names}")

    # Print the number of items in a list
    print("\nGet the Number of Items in a List\n----------------------------------")
    print(f"Items in Integer List: {len(integers)}")
    print(f"Items in Names List: {len(names)}")
    print(f"Items in Empty List: {len(empty)}")

    # Print values at specific indices 
    print("\nGet Values at Specific Indices in a list\n-----------------------------------------")
    print(f"First item in names lst: {names[0]}")
    print(f"Fourth item in names list: {names[3]}")

    # Print all items in a list
    print("\nPrinting All Names\n-------------------")
    for name in names:
        print(name)

    print("\nPrinting All Names with Index Values\n---------------------------------")
    for index in range(len(names)):
        print(f"{index}: {names[index]}")

    # Calculate the sum of all values in a list
    print(f"\nIntegers List: {integers}")
    sum = 0
    for integer in integers:
        sum += integer
    print(f"Sum of all integers: {sum}")

    # Calculate the average of all integers in a list
    avg = sum / len(integers)
    print(f"Average of all integers: {avg:.2f}")
    
    # Find the largest value in a last
    # Set max_value to the firdt item in the list
    max_value = integers[0]

    # Loop over the entire list
    for value in integers:
        # if value > max_value, set max_value to value
        if value > max_value:
            max_value = value

    # After the loop is done print the largest value
    print(f"Largest integer: {max_value}")
    
    # Does the list contain a specific item
    search_name = "Alice"
    if search_name not in names:
        print(f"\n{search_name} is not in the names list.")
    else:
        print(f"\n{search_name} is in the names list.")

main()
