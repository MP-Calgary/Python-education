import os
# clear the terminal 
os.system('clear')

import json

# Open the JSON file and read its contents into a string
with open('lab02.json', 'r') as file:
    data_str = file.read()

# Convert the string into a JSON object
data = json.loads(data_str)

# Extract the usernames and passwords into separate lists
usernames = data['username']
passwords = data['password']

# Print the lists to verify that the program works
# print(usernames)
# print(passwords)

inputname = input("Enter username: ")
inputpassword = input("Enter password: ")

# print(inputname)
# print(inputpassword)

if inputname in usernames:
    index = usernames.index(inputname)
    # print(inputname + " exists in the list at postion " + str(index))
    # print("Password for index " + str(index) + " is: " + passwords[index])
    if inputpassword == passwords[index]:
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")
else:
    # print(inputname + " does not exist in the list.")
    # for security reason, may want the same response brews a bad password
    print("You are not authorized to use the system.")