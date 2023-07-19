import os
import platform
def clear_terminal():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
# start the program with a clear terminal
clear_terminal()

#in operator working

list1= [1,2,3,4,5]
string1= "My name is AskPython"
tuple1=(11,22,33,44)

print("list1: ", list1)
print("5 in list1: ", 5 in list1) #True
print("5 not in list1: ", 5 not in list1) #True
print()

print("string1: ", string1)
print("is in string1: ", "is" in string1) #True
print("is not in string1: ", "is" not in string1) #True
print()

print("tuple1: ", tuple1)
print("88 in tuple1: ",88 in tuple1) #False
print("88 in not tuple1: ",88 not in tuple1) #False
print()

#in and not in operator working on Dictionary
 
dict1 = {1: "one", 2: "two", 3: "three", 4: "four"}

print("dict1: ", dict1)
 
print("one in dict1: ","one" in dict1)
print("one not in dict1: ", "one" not in dict1)
 
print("3 in dict1: ", 3 in dict1)
print("3 not in dict1: ",3 not in dict1)
 
print("5 in dict1: ", 5 in dict1)
print("5 not in dict1: ", 5 not in dict1)
print()

print("the in statement looks at the keys, not the values of dict")
print()


prices  = [17.91, 19.71, 18.55, 18.39, 19.01, 20.12, 19.87]
mon_fri = prices[1:6]
print (mon_fri)

prices    = [17.91, 19.71, 18.55, 18.39, 19.01, 20.12, 19.87]
wed_price = prices[3]
print(wed_price)

prices     = [17.91, 19.71, 18.55, 18.39, 19.01, 20.12, 19.87]
all_prices = [x for x in prices]
print(all_prices)

prices = [17.91, 19.71, 18.55, 18.39, 19.01, 20.12, 19.87]
high_prices = [x for x in prices if x>18]
print(high_prices)

prices     = [17.91, 19.71, 18.55, 18.39, 19.01, 20.12, 19.87]
three_days = [wday[1] for wday in enumerate(prices) if wday[0] in [1, 3, 5]]
print(three_days)
print()

x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))
print()

languages = ['Python', 'Java', 'JavaScript']

# The enumerate() function adds a counter to an iterable and returns it (the enumerate object).
enumerate_prime = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_prime))
print()

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# The syntax of enumerate() is:

# enumerate(iterable, start=0)
# enumerate() Arguments
# The enumerate() function takes two arguments:

# iterable - a sequence, an iterator, or objects that support iteration
# start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start.

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
print()

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print()

for count, item in enumerate(grocery):
  print(count, item)

print()

# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)

print()

# List Comprehension
# long way
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print()

# better, shorter way
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)