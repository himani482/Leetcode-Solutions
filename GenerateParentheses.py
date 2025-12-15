#22. Generate Parentheses
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        print(n)
        res =[]
        def rec(curr_str,open_c, close):
            print(curr_str)
            if open_c == n and close == n :
                res.append(curr_str)
                return res
            
            if open_c < n:
                rec(curr_str + '(', open_c + 1, close)
            if close < open_c :
                rec( curr_str + ")", open_c , close+1)
            
        rec("", 0,0)
        return res
