from utils import calculate_runtime

# Bubblesort

def bubble_sort_optimized(arr):
    iterations = 0
    # going to right
    for i in range(len(arr)):
        # going to left
        for j in range(len(arr) - i - 1):
            iterations += 1
            
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr, iterations

arr = [9,8,7,6,5,4,3,2,1]

print("Bubble sort optimized runtime: ")
print(calculate_runtime(bubble_sort_optimized, arr),bubble_sort_optimized(arr))

def swap(arr,i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort_unoptimized(arr):
    iterations = 0
    
    for i in arr:
        for j in range(len(arr) - 1):
            iterations += i
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

    return arr, iterations
                    
print("Bubble sort unoptimized runtime: ")
print(calculate_runtime(bubble_sort_unoptimized, arr),bubble_sort_unoptimized(arr))

# Insertion sort
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1 
        arr[i + 1] = key
    return arr

print("Insertion sort runtime: ")
print(calculate_runtime(insertion_sort, arr),insertion_sort(arr))

