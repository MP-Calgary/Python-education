import json
import os
# clear the terminal 
os.system('clear')

# Prompt the user for the file path of an alphabetically ordered collection of words in JSON format
file_path = input("Enter the file path for the word list in JSON format: ")

print(file_path)

# see if file exists
check_file = os.path.isfile(file_path)

if check_file == True:

# test file used was: Lab06.languages.json
# Read the JSON file into a dictiomary called "word_list"
    with open(file_path, "r") as f:
        word_list = json.load(f)
    f.close()

    # print("loaded word list: ", word_list)

    # print("Array values: ",word_list["array"])

    # convert the dictionary into a list, so can search by index
    array_values = word_list["array"]
    # print("Array list: ", array_values)

    # example to print out an exact item in list
    # print("Array 5: ", array_values[5])

    # Prompt the user for the word to search for and store it in a variable named "search_word"
    search_word = input("Enter the word to search for: ")

    # Set the variables "min_index" and "max_index" to 0 and the length of "word_list" - 1 respectively
    min_index = 0
    max_index = len(array_values) - 1

    # print("max index ", max_index)

    # Flag to keep track if word is found
    found = False

    # While "min_index" is less than or equal to "max_index":
    while min_index <= max_index and not found:
        # Set "mid_index" to the integer division of ("min_index" + "max_index") by 2
        mid_index = (min_index + max_index) // 2
        # print("mid_index is: ", mid_index)

        # If "word_list[mid_index]" is equal to "search_word":
        if array_values[mid_index] == search_word:
            # Print "The word is found at index " + mid_index
            print("The word is found at index", mid_index)
            # Set flag to True
            found = True
        # Else if "word_list[mid_index]" is less than "search_word":
        elif array_values[mid_index] < search_word:
            # Set "min_index" to "mid_index" + 1
            min_index = mid_index + 1
        # Else:
        else:
            # Set "max_index" to "mid_index" - 1
            max_index = mid_index - 1

    # If the word was not found, print appropriate message
    if not found:
        print("The word is not found in the list")
else:
    print(f"The file {file_path} does not exist.")