# Q2. Daily Temperatures
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # next greatest 
        st =[]
        
        n = len(temperatures)
        res =[0] * n

        for i in range(n-1,-1,-1):
            while ( st and  temperatures[st[-1]] <= temperatures[i]):
                st.pop()
            
            if st:
                
                res[i] = st[-1] - i

            st.append(i)
        return res
        # for i in range(n):
        #     if ns[i] != -1:
        #         res[i] =  ns[i] - i
        # return res
            


        

            
