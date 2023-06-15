import os
os.system('clear')  # clear the terminal 

# # input list
# lst = ["Hello", 10, "TutorialsPoint", 20, "python", "code"]

# # Checking if {TutorialsPoint} element in list using in operator
# print("lst: ", lst)
# print("Is 'TutorialsPoint' in lst: ", "TutorialsPoint" in lst)

# # Checking if {bigdata} element in list using in operator
# print("Is 'bigdata' in lst: ", "bigdata" in lst)
# print()

# # input list
# lst = [["Hello", 10], ["TutorialsPoint", 20], ["python", "code"]]

# # Checking if {TutorialsPoint,20} elements list present in nested list using in operator
# print("lst: ", lst)
# print("Is '[TutorialsPoint',20] in lst: ", ["TutorialsPoint",20] in lst)

# # Checking if {TutorialsPoint,code} elements list present in nested list using in operator
# print("Is '[TutorialsPoint','code'] in lst: ", ["TutorialsPoint","code"] in lst)
# print()

# # input list
# lst = ["Hello", 10, "TutorialsPoint", 20, "python", "code"]

# # Checking if {TutorialsPoint} element in list using in operator
# print("lst: ", lst)
# if "TutorialsPoint" in lst:
#    print('{TutorialsPoint} Element is in the given list')

# # Checking if {bigdata} element in list using in operator
# if "bigdata" in lst:
#    print('{bigdata} Element is in the given list')

# # If {bigdata} is not in list
# else:
#    print('{bigdata} Element is not present in the given list')

# print()

# For loop from 0 to 2, therefore running 3 times.
# for x in range(0, 3):
#     print("We're on time %d" % (x))

# Nested loops
# When you have a block of code you want to run x number of times, then a block of code within that code which you want to run y number of times,
# you use what is known as a "nested loop". In Python, these are heavily used whenever someone has a list of lists - an iterable object within an iterable object.
# for x in range(1, 11):
#     for y in range(1, 11):
#         print('%d * %d = %d' % (x, y, x*y))

# for x in range(3):  # The range function generates a sequence of numbers starting from 0 up to, but not including, the specified value (in this case, 3). So, the sequence generated is 0, 1, 2.
#     print("x= ",x)

# Early exits
# Like the while loop, the for loop can be made to exit before the given object is finished. 
# This is done using the break statement, which will immediately drop out of the loop and continue execution at the 
# first statement after the block. You can also have an optional else clause, which will run should the for loop exit cleanly - that is, without breaking.
# for x in range(3): 
#     print("x= ",x)
#     if x == 1:
#         break   # this will exit as x =1

#  For..Else
# for x in range(3):
#     print(x)
# else:
#     print('Final x = %d' % (x))

# Strings as an iterable
# string = "Hello World"
# for x in string:
#     print(x)

# Lists as an iterable
# collection = ['hey', 5, 'd']
# for x in collection:
#     print(x)

# Loop over Lists of lists
# list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for list in list_of_lists:
#     for x in list:
#         print(x)

# ----------------------------------------------------------------
# BAD SYNTAX
# mylist = ['a', 'b', 'c', 'd']
# for i in range(len(mylist)):
#     # do something with mylist[i]

# Better SYNTAX
# mylist = ['a', 'b', 'c', 'd']
# for v in mylist:
#     # do something with v

# ----------------------------------------------------------------

# learning about iterators
# define a list
# my_list = [4, 7, 0]

# # create an iterator from the list
# iterator = iter(my_list)

# # get the first element of the iterator
# print(next(iterator))  # prints 4

# # get the second element of the iterator
# print(next(iterator))  # prints 7

# # get the third element of the iterator
# print(next(iterator))  # prints 0

# ----------------------------------------------------------------

# the difference between iterable and iterator
# Iterable:
# An iterable is anything that you can iterate over, meaning you can loop through its elements one by one. Examples of iterables include lists, tuples, strings, dictionaries, and even files. 
# When you use a "for" loop to iterate over an iterable, Python automatically creates an iterator for that iterable behind the scenes.

# Iterator:
# An iterator is an object that represents a stream of data or a sequence of elements. It's responsible for keeping track of the current element and providing the next element in the sequence. 
# Iterators have two main methods: __iter__() and __next__(). The __iter__() method returns the iterator object itself, and the __next__() method returns the next element in the sequence. 
# If there are no more elements, it raises a StopIteration exception.

# The key difference between an iterable and an iterator is that an iterable is a collection of items that can be iterated over, 
# while an iterator is an object that controls the iteration process and keeps track of the current state.

# To summarize, think of an iterable as a container or source of data, and an iterator as a tool that allows you to access the elements of that container one by one. 
# When you use a "for" loop or other constructs like list comprehensions or generator expressions, 
# Python automatically handles the creation of an iterator for the iterable you're working with, making it easy to loop through the elements.