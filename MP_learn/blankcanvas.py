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

print("This is regular")
print(color.BOLD + 'THIS IS BOLD' + color.END)
print(color.PURPLE + 'This IS PURPLE!' + color.END)
print(color.CYAN + 'This IS CYAN!' + color.END)
print(color.DARKCYAN + 'This IS DARKCYAN!' + color.END)
print(color.BLUE + 'This IS BLUE!' + color.END)
print(color.GREEN + 'This IS GREEN!' + color.END)
print(color.YELLOW + 'This IS YELLOW!' + color.END)
print(color.RED + 'This IS RED!' + color.END)
print(color.UNDERLINE + 'UNDERLINE IS HERE!' + color.END)
print("This is regular")