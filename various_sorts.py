import os
os.system('clear')  # clear the terminal 

def bubble_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n-1):
        for j in range(n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return steps

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

# def counting_sort(arr):
#     n = len(arr)
#     output = [0] * n
#     count = [0] * (max(arr) + 1)
#     steps = 0
#     for i in range(n):
#         steps += 1
#         count[arr[i]] += 1
#     for i in range(1, len(count)):
#         steps += 1
#         count[i] += count[i-1]
#     for i in range(n-1, -1, -1):
#         steps += 1
#         output[count[arr[i]] - 1] = arr[i]
#         count[arr[i]] -= 1
#     for i in range(n):
#         arr[i] = output[i]
#     return steps

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

def radix_sort(arr):
    steps = 0
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        steps += counting_sort_by_digit(arr, exp)
        exp *= 10
    return steps

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

# Test data
# data = [31, 72, 10, 32, 18, 95, 25, 50]
data = [103,11,22,31, 72, 67, 10, 32, 2, 18, 95, 9, 25, 86,50]

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