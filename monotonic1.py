# Q1. Final Prices With a Special Discount in a Shop
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #  finding next smallest
        res =[]
        st =[]
        
        n = len(prices)
        ns=[-1] * n
        for i in range(n-1, -1,-1):
            while st and st[-1] > prices[i]:
                st.pop()
            
            if st :
                ns[i] = st[-1]
            
            st.append(prices[i])
        
        for i in range(n):
            if ns[i] != -1:
                val = prices[i]  - ns[i]
                res.append(val)
            else:
                res.append(prices[i])
        return res
