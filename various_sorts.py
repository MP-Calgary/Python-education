import os
os.system('clear')  # clear the terminal 
import random

# Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly swapping adjacent elements 
# if they are in the wrong order until the entire array is sorted. The largest (or smallest, depending on the sorting order) 
# element "bubbles" to the end of the array in each pass. This process is repeated until the array is completely sorted.
def bubble_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n-1):
        for j in range(n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return steps

# Selection Sort is a comparison-based sorting algorithm. It divides the input array into two parts: 
# the sorted part and the unsorted part. Initially, the sorted part is empty. The algorithm repeatedly selects the smallest 
# (or largest) element from the unsorted part and swaps it with the leftmost element of the unsorted part. 
# This process continues until the entire array is sorted.
def selection_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return steps

# Insertion Sort is comparison-based sorting algorithm that builds the final sorted array
# one element at a time. It starts with the second element and compares it with the elements before it, 
# shifting the greater elements one position to the right. This process continues until the entire array is sorted.
def insertion_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            steps += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return steps

# Merge Sort is a divide-and-conquer algorithm that works by repeatedly dividing the input array into smaller halves, 
# sorting them, and then merging them back together. It divides the array into two halves until each half contains 
# only one element (which is inherently sorted). Then it merges the sorted halves by repeatedly comparing 
# the elements and placing them in the correct order.
def merge_sort(arr):
    steps = 0
    if len(arr) <= 1:
        return arr, steps
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left, left_steps = merge_sort(left)
    right, right_steps = merge_sort(right)
    merged, merge_steps = merge(left, right)
    steps += left_steps + right_steps + merge_steps
    return merged, steps

# needed for merge_sort
def merge(left, right):
    merged = []
    steps = 0
    while left and right:
        steps += 1
        if left[0] <= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
    while left:
        merged.append(left[0])
        left = left[1:]
    while right:
        merged.append(right[0])
        right = right[1:]
    return merged, steps

# Quick Sort is a divide-and-conquer algorithm. It selects a pivot element from the array and partitions the other 
# elements into two sub-arrays, according to whether they are less than or greater than the pivot. 
# The sub-arrays are then recursively sorted. The pivot element is positioned correctly in the final sorted array. 
# This process is repeated for each sub-array until the entire array is sorted.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr, 0  # Return sorted array and 0 steps if array is already sorted
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort subarrays and count the steps
    left, left_steps = quick_sort(left)
    right, right_steps = quick_sort(right)
    
    # Calculate total steps
    steps = len(arr) - 1 + left_steps + right_steps
    
    return left + middle + right, steps

# needed for heap_sort
def heapify(arr, n, i, steps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps += 1
        steps = heapify(arr, n, largest, steps)
    return steps

# Heap Sort uses a binary heap data structure to sort elements. First, it builds a max heap 
# (for sorting in ascending order) or a min heap (for sorting in descending order) from the input array. 
# Then it repeatedly extracts the root element (the maximum or minimum element, depending on the heap type),
# places it at the end of the sorted array, and restructures the heap. This process continues until the entire array is sorted.
def heap_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n//2 - 1, -1, -1):
        steps = heapify(arr, n, i, steps)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps = heapify(arr, i, 0, steps)
        steps += 1
    return steps

# Counting Sort is a non-comparison-based sorting algorithm that works well when the range of input values is small. 
# It works by counting the frequency of each distinct element in the input array, creating a count array. 
# Then it modifies the count array to store the actual position of each element in the output array. 
# Finally, it iterates through the input array, placing each element in 
# its correct position in the output array based on the modified count array.
def counting_sort(arr):
    n = len(arr)
    output = [0] * n
    count = [0] * (max(arr) + 1)
    steps = 0
    for i in range(n):
        steps += 1
        count[arr[i]] += 1
    for i in range(1, len(count)):
        steps += 1
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        steps += 1
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(n):
        arr[i] = output[i]
    return arr, steps

# Radix Sort is a non-comparison-based sorting algorithm. It sorts the elements by their individual digits or bits. 
# It starts by sorting the elements based on the least significant digit (or bit), 
# then proceeds to the next significant digit (or bit), and so on, until all digits or bits have been considered. 
# Radix Sort can use Counting Sort or other stable sorting algorithms as a subroutine to sort each digit or bit.
def radix_sort(arr):
    steps = 0
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        steps += counting_sort_by_digit(arr, exp)
        exp *= 10
    return steps

# needed for radix_sort
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    steps = 0
    for i in range(n):
        steps += 1
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        steps += 1
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        steps += 1
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    for i in range(n):
        arr[i] = output[i]
    return steps

# want to generate a random list of numbers that can be test the sorting algoriths
# takes a paramter of how many numbers in the list.
# for now, the list is betwen 1 and 500
def generate_random_list(num_integers):
    random_list = []
    for _ in range(num_integers):
        random_list.append(random.randint(1, 500))
    return random_list

num_integers = 8  # Number of integers to generate in the set

data = generate_random_list(num_integers)

# Test data if want to fix to a pre-defined list
# data = [31, 72, 10, 32, 18, 95, 25, 50]

# original list
print("Original list:", data)
print()

# Bubble Sort
bubble_sorted = data.copy()
bubble_steps = bubble_sort(bubble_sorted)
print("Bubble Sort:", bubble_sorted, "     steps: ",bubble_steps)
print()

# Selection Sort
selection_sorted = data.copy()
selection_steps = selection_sort(selection_sorted)
print("Selection Sort:", selection_sorted, "     steps: ",selection_steps)
print()

# Insertion Sort
insertion_sorted = data.copy()
insertion_steps = insertion_sort(insertion_sorted)
print("Insertion Sort:", insertion_sorted, "     steps: ",insertion_steps)
print()

# Merge Sort
merge_sorted, merge_steps = merge_sort(data.copy())
print("Merge Sort:", merge_sorted, "     steps: ",merge_steps)
print()

# Quick Sort
quick_sorted, quick_steps = quick_sort(data.copy())
print("Quick Sort:", quick_sorted, "     steps: ",quick_steps)
print()

# Heap Sort
heap_sorted = data.copy()
heap_steps = heap_sort(heap_sorted)
print("Heap Sort:", heap_sorted, "     steps: ",heap_steps)
print()

# Counting Sort
counting_sorted, counting_steps = counting_sort(data.copy())
print("Counting Sort:", counting_sorted, "     steps: ",counting_steps)
print()

# Radix Sort
radix_sorted = data.copy()
radix_steps = radix_sort(radix_sorted)
print("Radix Sort:", radix_sorted, "     steps: ",radix_steps)
print()