'''Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.'''
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False

        for i in range(n - 2 * k + 1):
            j = i + k
            val1 = nums[i:i + k]
            val2 = nums[j:j + k]
            print(val1)
            print(val2)
            if (val1 == sorted(val1) and len(set(val1)) == k ) and (val2 == sorted(val2) and len(set(val2)) == k):
                return True
        return False
