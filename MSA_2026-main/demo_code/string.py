def main():
    my_name = "collin"
    
    # Capitalize a string
    print(f"My name capitalized: {my_name.capitalize()}")

    # Make a string uppercased
    print(f"My name uppercased: {my_name.upper()}")

    # Make a string lowercased
    last_name = "KNIGHT"
    print(f"My full name lowercased: {my_name.lower()} {last_name.lower()}")

    # Compare two strings
    my_name_title_case = "Collin"

    if my_name.lower() == my_name_title_case.lower():
        print("The strings are equal.")
    else:
        print("The strings are not equal.")

    # Determine if a string starts with a set of characters
    print("\nUsing the Startswith() Method\n------------------------------")
    print(f"{my_name} starts with a C or c: {my_name.startswith("C") or my_name.startswith("c")}")

    if not my_name.startswith("Coll") and not my_name.startswith("coll"):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly.")

    if not my_name.lower().startswith("coll"):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly.")
    
    # Determine if a string ends with a set of characters
    print("\nUsing the Endswith() Method\n----------------------------")
    print(f"{my_name} ends with 'llin': {my_name.endswith("llin")}")
    
    # Find the l in Collin
    print("\nUsing the Find() Method\n------------------------")
    search_letter = "in"
    index_of_substring = my_name.find(search_letter)
    
    if index_of_substring != -1:
        print(f"The '{search_letter}' is at index {index_of_substring} in {my_name}")
    else:
        print(f"There is no '{search_letter}' in {my_name}")

    # Print each letter of a string
    print("\nLooping through a string\n-------------------------")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters.\n")
    # Print the letters in a string along with the index position
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]}")

    # Search a string for the number of substrings
    print("\nSearch a String\n--------------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    # Count the number of occurences of the word dog in the sentence
    # Expected Output: 3
    count = 0
    index = sentence.find("dog")

    while index != -1:
        print(index)
        count += 1
        index = sentence.find("dog", index + 1)

    print(count)
        
        
main()
