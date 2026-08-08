#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

#Example 1:

#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]

        def genrate(current, open_b, close_b):
            if len(current ) ==  2 * n:
                res.append(current)
                return 
            

            if open_b < n:
                genrate( current + "(" , open_b + 1, close_b)
            
            if close_b < open_b:
                genrate(current + ")", open_b, close_b + 1)

            
        genrate("",0, 0 )
        return res
