from utils import calculate_runtime

# Linear Search
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [2,5,8,9,10, 22, 25]
target = 10
print("Search Algorithm runtime: ")
print(calculate_runtime(search, arr, target), search(arr,target))

# Binary Search of ordered list
def binary_search(arr, start, end, target):
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] < target:
            start = middle + 1
        elif arr[middle] > target:
            end = middle - 1
        else:
            # return assuming arr[middle] is equal to target
            print(f"target is {target} and middle is {arr[middle]} at the index {middle}")
            return middle
    return -1

#print(calculate_runtime(binary_search, arr,0, len(arr)-1, target))
print("Binary Algorithm Interative runtime: ")
print(calculate_runtime(binary_search,arr,0, len(arr)-1, target), binary_search(arr,0, len(arr)-1, target))

def binary_recur(arr, start, end, target):
    if end >= start:

        middle = start + end - 1 // 2

        if arr[middle] < target:
            binary_recur(arr, middle + 1, end, target)

        elif arr[middle] > target:
            
            return binary_recur(arr, start, middle - 1, target)
        else:
            print(f"target is {target} and middle is {arr[middle]} at the index {middle}")
            return middle
    else:
        return -1


print("Binary Algorithm Recursion runtime: ")
print(calculate_runtime(binary_recur,arr,0, len(arr)-1, target), binary_recur(arr,0, len(arr)-1, target))


    
        
    

