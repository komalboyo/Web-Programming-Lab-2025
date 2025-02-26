def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Smallest element:", find_smallest(arr))
