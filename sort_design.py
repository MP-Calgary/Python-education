import os
os.system('clear')  # clear the terminal 

def sort_array(array):
    n = len(array)
    if n <= 1:
        return array
    
    for i_pivot in range(n - 1, 0, -1):
        i_largest = 0
        for i_check in range(1, i_pivot + 1):
            # print("ipivot: ",i_pivot,"  i_largest: ", i_largest, "  i_check: ",i_check)
            if array[i_check] > array[i_largest]:
                i_largest = i_check
        
        if array[i_largest] > array[i_pivot]:
            array[i_pivot], array[i_largest] = array[i_largest], array[i_pivot]
        # print("  ", array)
    
    return array

# Example usage
# unsorted_array = [31, 72, 10, 32, 18, 95, 25, 50]
# unsorted_array = [26, 6, 90, 55]

import random
def generate_random_list(num_integers):
    random_list = []
    for _ in range(num_integers):
        random_list.append(random.randint(1, 500))
    return random_list

num_integers = 8  # Number of integers to generate in the set

unsorted_array = generate_random_list(num_integers)

print("original array: ", unsorted_array)
print()
sorted_array = sort_array(unsorted_array)
print()
print("sorted array: ", sorted_array)
