# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times

# COUNTING SORT.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count= [0] * (n+1)

        for i in citations:
            if i >= n :
                count[n] += 1
            else:
                count[i] += 1

        total = 0
        for i in range(n , -1, -1):
            total += count[i]
            if total >= i:
                return i
