class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in nums:
                if i in curr:
                    continue
                curr.append(i)
                backtrack(curr)
                curr.pop()
        backtrack([])
        return res
        
