# print(" ")
# import math            
# num = 4
# print("srq answer: ", math.sqrt(num))

# print(" ")

# import matplotlib

# print("matplotlib version: ",matplotlib.__version__)
# print(" ")

# import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# # print(myvar)
# print(" ")
# print("pandas version: ",pd.__version__)


# # import pandas as pd

# df = pd.read_json('data.json')

# # print(df.to_string()) 

# print(" ")

# import tkinter
# window = tkinter.Tk()
# top.title('Hello Python')
# top.geometry("300x200+10+20")
# top.mainloop()

# window = Tk()

# window.title("Welcome to LikeGeeks app")

# window.geometry('350x200')

# lbl = Label(window, text="Hello")

# lbl.grid(column=0, row=0)

# txt = Entry(window,width=10)

# txt.grid(column=1, row=0)

# def clicked():

#     res = "Welcome to " + txt.get()

#     lbl.configure(text= res)

# btn = Button(window, text="Click Me", command=clicked)

# btn.grid(column=2, row=0)

# window.mainloop()

# user = {'username': 'johndoe', 'email': 'johndoe@example.com', 'age': 35}

# username = user['username']

# print(username)

# Sample dictionary list
# data = [
#     {'name': 'John', 'age': 25},
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob', 'age': 35}
# ]

# # Index of the dictionary to access
# index = 1

# # Access the dictionary at the specified index
# if index < len(data):
#     dictionary = data[index]
#     print(f"Dictionary at index {index}: {dictionary}")
# else:
#     print("Index out of range.")

# print()
# print("reference a function in another file")
# columns_data = [['Date', '2015/11/25', '2015/11/30', '2015/12/07', '2015/12/11', '2015/12/15'],
#                 ['Client', 'RandP', 'GOA', 'Robots and Pencils', 'AHS', 'Decisive Farming'],
#                 ['Project', 'r&p-robofactory-pm/ba guild', 'goa-rmas0049-firebans', 'sales-goa queens printer ministry', 'ahs-wait times-ios', 'decisive-scouting'],
#                 ['Project Code', '013', '066', '112', '040', '095'],
#                 ['Hours', 8.5, 6.5, 1.5, 3, 2]]

# from useful_functions import display_table

# display_table(columns_data)

import os
import sys
os.system('clear')

# if sys.platform.startswith('darwin'):  # Check if running on macOS
#     # Prompt the user to select a file using the command line
#     file_path = os.popen('osascript -e \'POSIX path of (choose file)\'').read().strip()

#     if file_path:
#         print("Selected file:", file_path)
#     else:
#         print("No file selected.")
# else:
#     print("This feature is only supported on macOS.")

# growth = [3, 1, 2, 4, 2, 3, 2]
# growth = [3, 1, 2, 4]
# print(growth)
# growth.sort()
# print(growth)
# # smallest_growth = sorted_list.pop[0]
# # print(f'The smallest growth in the week is: {smallest_growth}cm')
# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1[::-1])

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# list1 = tuple1[1]
# print(list1)
# num = list1[1]
# print(num)
# understand indexing
# tuple1[0] = 'Orange'
# tuple1[1] = [10, 20, 30]
# list1[1][1] = 20
# tuple1 = (50,)
# print(tuple1)

# tuple1 = (10, 20, 30, 40)
# var1 = tuple1[0]
# print(var1)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   REVERSE = '\033[7m'
   END = '\033[0m'

# print("This is regular")
# print(color.BOLD + 'THIS IS BOLD' + color.END)
# print(color.PURPLE + 'This IS PURPLE!' + color.END)
# print(color.CYAN + 'This IS CYAN!' + color.END)
# print(color.DARKCYAN + 'This IS DARKCYAN!' + color.END)
# print(color.BLUE + 'This IS BLUE!' + color.END)
# print(color.GREEN + 'This IS GREEN!' + color.END)
# print(color.YELLOW + 'This IS YELLOW!' + color.END)
# print(color.RED + 'This IS RED!' + color.END)
# print(color.UNDERLINE + 'UNDERLINE IS HERE!' + color.END)
# print("This is regular")

# import random

# # Constants for item names
# OPIUM = 0
# SILK = 1
# ARMS = 2
# GENERAL = 3

# # Dictionary to map item names to their price lists
# base_price = {
#     OPIUM: [1000, 11, 16, 15, 14, 12, 10, 13],
#     SILK:  [100,  11, 14, 15, 16, 10, 13, 12],
#     ARMS:  [10,   12, 16, 10, 11, 13, 14, 15],
#     GENERAL: [1,    10, 11, 12, 13, 14, 15, 16]
# }

# # Array of port names
# portNames = ["Hong Kong", "Batavia", "Calcutta", "Jambi", "Muscat", "Penang", "Rangoon", "Surat"]

# def set_prices(portIndex):
#    global base_price

#    port = portIndex # - 1  # Adjust portIndex to match Python list indexing (0-based)

#    for num in range(1, 11):
#       op1 = base_price[OPIUM][port]
#       base1 = base_price[OPIUM][0]
#       calc1 = (base_price[OPIUM][port] // 2) * (random.randint(1, 3))

#    price_opium = base_price[OPIUM][port] // 2 * (random.randint(1, 3)) * base_price[OPIUM][0]
#    price_silk = base_price[SILK][port] // 2 * (random.randint(1, 3)) * base_price[SILK][0]
#    price_arms = base_price[ARMS][port] // 2 * (random.randint(1, 3)) * base_price[ARMS][0]
#    price_general = base_price[GENERAL][port] // 2 * (random.randint(1, 3)) * base_price[GENERAL][0]
#    return [price_opium, price_silk, price_arms, price_general]

# # Example usage:
# portIndex = 1  # Choose a port index (1 to 8)
# prices = set_prices(portIndex)
# print("Port:", portNames[portIndex - 1])  # Print the chosen port name
# print("My Prices:", prices)


import random

# Constants for item names
OPIUM = "Opium"
SILK = "Silk"
ARMS = "Arms"
GENERAL = "General"

# Dictionary to map item names to their price lists
base_price = {
    OPIUM: [1000, 11, 16, 15, 14, 12, 10, 13],
    SILK:  [100,  11, 14, 15, 16, 10, 13, 12],
    ARMS:  [10,   12, 16, 10, 11, 13, 14, 15],
    GENERAL: [1,    10, 11, 12, 13, 14, 15, 16]
}

# Function to calculate random price based on location's rank
def generate_random_price(item_name):
    max_price, *location_factors = base_price[item_name]
    location_rank = location_factors.index(max(location_factors)) + 1
    min_range = 0
    max_range = max_price
    if item_name == OPIUM:
        max_range = max_price - (location_rank * 5)
    elif item_name == SILK:
        max_range = max_price - (location_rank * 1)
    elif item_name == ARMS:
        max_range = max_price - (location_rank * 5)
    elif item_name == GENERAL:
        max_range = max_price - (location_rank * 1)
    return random.randint(min_range, max_range)

def set_prices(portIndex):
    global base_price

    port = portIndex - 1  # Adjust portIndex to match Python list indexing (0-based)

    price_opium = base_price[OPIUM][port] // 2 * generate_random_price(OPIUM)
    price_silk = base_price[SILK][port] // 2 * generate_random_price(SILK)
    price_arms = base_price[ARMS][port] // 2 * generate_random_price(ARMS)
    price_general = base_price[GENERAL][port] // 2 * generate_random_price(GENERAL)

    return [price_opium, price_silk, price_arms, price_general]

# Example usage:
portIndex = 3  # Choose a port index (1 to 8)
prices = set_prices(portIndex)
print("Prices:", prices)
