# Write a Python class to find a pair of elements (indices of the two numbers) from a given array 
# whose sum equals a specific target number.
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4

class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_pair(self):
        num_dict = {}
        for i, num in enumerate(self.numbers):
            complement = self.target - num
            if complement in num_dict:
                return num_dict[complement], i
            num_dict[num] = i
        return None

arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

indices = PairFinder(arr, target)
result = indices.find_pair()
if result:
    print(f"Output: {result[0]+1}, {result[1]+1}")
else:
    print("None")