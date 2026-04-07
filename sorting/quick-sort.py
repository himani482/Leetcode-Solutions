# Quick Sort (short):
#
# Pick a pivot → place smaller elements left, larger right → repeat
#
# Time:
# Avg: O(n log n)
# Worst: O(n²)

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr

            pivot = arr[len(arr) // 2]

            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            # print(left,mid, right)

            return quick_sort(left) + mid + quick_sort(right)

        return quick_sort(nums)


#  can also be done in space complexity of O(n)
