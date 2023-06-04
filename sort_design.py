import os
os.system('clear')  # clear the terminal 

def sort_array(array):
    n = len(array)
    if n <= 1:
        return array
    
    for i_pivot in range(n - 1, 0, -1):
        i_largest = 0
        for i_check in range(1, i_pivot + 1):
            if array[i_check] > array[i_largest]:
                i_largest = i_check
        
        array[i_pivot], array[i_largest] = array[i_largest], array[i_pivot]
        # print("  ", array)
    
    return array

# Example usage
unsorted_array = [31, 72, 10, 32, 18, 95, 25, 50]
print("original array: ", unsorted_array)
print()
sorted_array = sort_array(unsorted_array)
print()
print("sorted array: ", sorted_array)
