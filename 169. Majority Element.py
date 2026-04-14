# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#1 -Boyer-Moore - Algo
#The algorithm operates on the concept of cancellation. If each majority element "cancels" one non-majority element, 
#the majority element will always be the "survivor" because it appears more than all other elements combined


 class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =0
        ans =0
        for i in nums:
            print(i, count ,ans)
            if count == 0:
                ans = i
            
            count += 1 if i == ans else -1

        return ans 
        
        
