# 167. Two Sum II - Input Array Is Sorted


# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = {numbers[0] : 1}
        n = len(numbers)
        for i in range(1,n):
            val = target - numbers[i]
            if val in ans:
                return [ans[val], i + 1]
            else:
                ans[numbers[i]] = i + 1
        return None
