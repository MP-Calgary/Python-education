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
data = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 35}
]

# Index of the dictionary to access
index = 1

# Access the dictionary at the specified index
if index < len(data):
    dictionary = data[index]
    print(f"Dictionary at index {index}: {dictionary}")
else:
    print("Index out of range.")

print()
print("reference a function in another file")
columns_data = [['Date', '2015/11/25', '2015/11/30', '2015/12/07', '2015/12/11', '2015/12/15'],
                ['Client', 'RandP', 'GOA', 'Robots and Pencils', 'AHS', 'Decisive Farming'],
                ['Project', 'r&p-robofactory-pm/ba guild', 'goa-rmas0049-firebans', 'sales-goa queens printer ministry', 'ahs-wait times-ios', 'decisive-scouting'],
                ['Project Code', '013', '066', '112', '040', '095'],
                ['Hours', 8.5, 6.5, 1.5, 3, 2]]

from useful_functions import display_table

display_table(columns_data)