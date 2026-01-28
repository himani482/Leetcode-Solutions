class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr =[]
        res =[]
        #  1
        def backtrack(ind):
            if ind == len(nums):
                res.append(curr [:])
                return

            curr.append(nums[ind])
            backtrack(ind + 1)
            curr.pop()

            backtrack(ind + 1)
        backtrack(0)
        return res

        # 2
        def backtrack(ind, curr):
            res.append(curr[:])
            for i in range(ind, len(arr)):
                curr.append(arr[i])
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0,[])
        return res