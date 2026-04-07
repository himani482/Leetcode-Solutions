# Algorithm
# First, we will select the range of the unsorted array using a loop (say i) that indicates the starting index of the range. The loop will run forward from 0 to n-1. The value i = 0 means the range is from 0 to n-1, and similarly, i = 1 means the range is from 1 to n-1, and so on. (Initially, the range will be the whole array starting from the first index.)
# Now, in each iteration, we will select the minimum element from the range of the unsorted array using an inner loop.
# After that, we will swap the minimum element with the first element of the selected range(in step 1).
# Finally, after each iteration, we will find that the array is sorted up to the first index of the range

#Time Complexity:O(N^2),Selection sort runs in O(N²) time in the best, average, and worst cases due to its nested loop structure
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_ind = i
            for j in range(i +1, n):
                if nums[j] < nums[min_ind]:
                    min_ind = j

            nums[min_ind], nums[i] = nums[i], nums[min_ind]
        return nums
