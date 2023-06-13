from tkinter import *


def input1(event):
    text = event.widget.cget("text")
    # print(text)

    if text == "=":  ## WHen = is pressed evaluate all the operations
        try:
            # evaluating the result for str
            result = eval(str(value.get()))
            value.set(result)
        except Exception as e:
            value.set("Error")
            print("error", e)

    elif text == "DEL":
        try:
            fullstring = value.get()   ## get the number from the screen
            newstring = fullstring.replace(fullstring[-1], "") ## Remove last digit
            value.set(newstring) ## set the new number as value

            # print(newstring) 
            entry1.update()  ## Enter the updated number    ## eg->  567 --> 56
        except Exception as e:
            print(e) 

    elif text == "C":
        value.set("")  ## set the screen as blank
        entry1.update()  ## update the screen
    else:
        value.set(value.get() + text)
        entry1.update()


root = Tk()
root.geometry("500x380")
root.title("Calculator")
root.wm_iconbitmap("profile.ico")
value = StringVar()
entryframe = Frame(root, borderwidth=3, relief=SUNKEN)
entry1 = Entry(entryframe, font="lucida 27 bold", textvariable=value)
entry1.pack()
entryframe.pack(pady=20, padx=5)

buttonframe = Frame(root,)

list1 = [
    "9",
    "8",
    "7",
    "C",
    "6",
    "5",
    "4",
    "/",
    "3",
    "2",
    "1",
    "*",
    "00",
    "0",
    ".",
    "-",
    "%",
    "DEL",
    "=",
    "+",
]
i = 0
for n in list1:
    button1 = Button(buttonframe, text=n, font="lucida 20 ", padx=35, width=1,)
    button1.grid(row=int(i / 4), column=i % 4)
    i = i + 1

    button1.bind("<Button-1>", input1)

buttonframe.pack()

root.mainloop()