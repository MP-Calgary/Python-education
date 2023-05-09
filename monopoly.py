import os
# clear the terminal 
os.system('clear')

print (os.getcwd())

# Set up the prompts
PA = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
NC = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
PC = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
Cash = int(input("How much cash do you have to spend? "))
Houses = int(input("How many houses are there to purchase? "))
Hotels = int(input("How many hotels are there to purchase? "))
Color_Group = input("Do you own all the green properties? (y/n) ")

# Calculate the cost of a hotel
hotel_cost = 200 + (4 * 200)

# Calculate the cost of the next house
if Houses == 0:
    house_cost = 0
else:
    house_cost = 200

# Determine if the player has enough money to build a hotel
if Cash < hotel_cost:
    print("You do not have sufficient funds to purchase a hotel at this time.")
    exit()

# Determine if there are enough houses available to purchase
if Houses < 4:
    print("There are not enough houses available for purchase at this time.")
    exit()

# Determine if there are enough hotels available to purchase
if Hotels < 1:
    print("There are not enough hotels available for purchase at this time.")
    exit()

# Determine if Pennsylvania already has a hotel
if PA == 5:
    print("You cannot purchase a hotel if the property already has one.")
    exit()

# Determine if the player owns all the green properties
if Color_Group == "n":
    if PC == 5:
        print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
        exit()
    elif NC == 5:
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
        exit()
    else:
        print("You cannot purchase a hotel until you own all the properties of a given color group.")
        exit()

# Calculate the number of houses to be placed on each property
if PA == 4:
    num_houses_PA = 0
    num_houses_NC = 4
    num_houses_PC = 0
else:
    num_houses_PA = 4
    num_houses_NC = 3
    num_houses_PC = 1

# Calculate the cost of the transaction
total_cost = hotel_cost + (num_houses_NC * house_cost)

# Determine if the player has enough money to make the transaction
if Cash < total_cost:
    print("You do not have sufficient funds to purchase a hotel at this time.")
    exit()

# Display the transaction details
print("This will cost $" + str(total_cost) + ".")
print("Purchase 1 hotel and " + str(num_houses_NC) + " house(s).")
print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
print("Put " + str(num_houses_PA) + " house(s) on North Carolina.")
print("Put " + str(num_houses_PC) + " house(s) on Pacific.")


Print("didn't actually add boardwalk yet")