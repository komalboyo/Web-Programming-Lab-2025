# Write a Python class to get all possible unique subsets from a set of distinct integers 
# Input:[4,5,6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

# class Subsets:
#     def __init__(self, nums):
#         self.nums = nums

#     def generate_subsets(self):
#         result = []
#         self._backtrack(0, [], result)
#         return result

#     def _backtrack(self, index, current, result):
#         if index == len(self.nums):
#             result.append(current[:])
#             return
#         current.append(self.nums[index])
#         self._backtrack(index + 1, current, result)
#         current.pop()
#         self._backtrack(index + 1, current, result)

# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# subsets = Subsets(nums)
# print(subsets.generate_subsets())

class Subsets:
    def __init__(self, nums):
        self.nums = nums

    def generate_subsets(self):
        result = [[]]
        for num in self.nums:
            result += [item + [num] for item in result]
        return result

nums = list(map(int, input("Enter numbers separated by space: ").split()))
subsets = Subsets(nums)
print(subsets.generate_subsets())
