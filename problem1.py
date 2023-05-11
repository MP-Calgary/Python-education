from typing import List

def sumList(l: List[int]) -> int:
    return sum(l)

def digitsOfInt(n: int) -> List[int]:
    if n <= 0:
        return []
    else:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        return digits[::-1]
    
def additivePersistence(n: int) -> int:
    if n < 10:
        return 0
    else:
        persistence = 0
        while n >= 10:
            n = sum(int(d) for d in str(n))
            persistence += 1
        return persistence

def digitalRoot(n: int) -> int:
    if n < 10:
        return n
    else:
        while n >= 10:
            n = sum(int(d) for d in str(n))
        return n

def listReverse(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Problem #1 A)
# Example usage for sumList
list1 = [1, 2, 3, 4]
list2 = [1,-2,3,5]
list3 = [1,3,5,7,9,11]

print(f"The sum of {list1} is {sumList(list1)}")
print(f"The sum of {list2} is {sumList(list2)}")
print(f"The sum of {list3} is {sumList(list3)}")

# Problem #1 B)
# Example usage for digitsOfInt
num1 = 12345
num2 = 987654321
num3 = 0
num4 = -123

print(f"The digits of {num1} are {digitsOfInt(num1)}")
print(f"The digits of {num2} are {digitsOfInt(num2)}")
print(f"The digits of {num3} are {digitsOfInt(num3)}")
print(f"The digits of {num4} are {digitsOfInt(num4)}")

# Problem #1 C)
# Example usage for digitsOfInt
n = 9876
persistence = additivePersistence(n)
root = digitalRoot(n)
print(f"The additive persistence of {n} is {persistence}")
print(f"The digital root of {n} is {root}")

# Problem #2 A)
# Example usage for listReverse
lst = [1, 2, 3, 4, 5]
reversed_lst = listReverse(lst)
print(f"The reversed list of {lst} is {reversed_lst}")

def palindrome(w):
    # Convert the string to a list of characters
    chars = list(w)
    # Reverse the list of characters
    reversed_chars = listReverse(chars)
    # Convert the reversed list back to a string
    reversed_w = "".join(reversed_chars)
    # Compare the original string with the reversed string
    return w == reversed_w


word1 = "racecar"
word2 = "hello"
print(f"{word1} is a palindrome: {palindrome(word1)}")
print(f"{word2} is a palindrome: {palindrome(word2)}")

#assignment 2
# problem A, Tail recursion

def assoc(d, k, l):
    def helper(l, acc):
        if not l:
            return d
        elif l[0][0] == k:
            return l[0][1]
        else:
            return helper(l[1:], acc)
    return helper(l, d)

# Example usage of the assoc function
key = "jeff"
default_val = -1
key_val_pairs = [("sorin", 85), ("jeff", 23), ("moose", 44)]

result = assoc(default_val, key, key_val_pairs)
print("Result of Assoc: ", result)

# Question B: Define the remove_duplicates function
def remove_duplicates(lst):
    res = []
    for item in lst:
        if not res.__contains__(item):
            res.append(item)
    return res[::-1]

# Example usage of the remove_duplicates function
input_list = [1, 6, 2, 4, 12, 2, 13, 6, 9]
unique_list = remove_duplicates(input_list)
print("Result of remove duplicates: ",unique_list)  # Output: [1, 6, 2, 4, 12, 13, 9]

# Quesiton C: 
def f(x):
    xx = x * x * x
    return (xx, xx < 100)

def wwhile(f_and_test, b):
    (f, test) = f_and_test
    (b_new, c) = f(b)
    if c:
        return wwhile((f, test), b_new)
    else:
        return b

result = wwhile((f, lambda x: True), 2)
print("Result of wwhile: ",result)  # Output: 512

# import matplotlib.pyplot as plt
# Partition = 'Holidays', 'Eating_Out', 'Shopping', 'Groceries'
# sizes = [250, 100, 300, 200]
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=Partition, autopct='%1.1f%%', shadow=True, startangle=90)         
# ax1.axis('equal')
# plt.show()

import tkinter
#try Tinker
# from tkinter import *
# main = Tk()
# main.mainloop()