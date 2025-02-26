# Write a python program to implement binary search with recursion

def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    return -1

arr = list(map(int, input("Enter numbers separated by space: ").split()))
e = int(input("Enter element to be searched: "))

print("Result: ", binary_search(arr, 0, len(arr)-1, e))
