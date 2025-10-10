class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # return res
        res =[]
        n = len(potions)
        potions.sort()

        for s in spells:
            # min_s = success / s
            min_s =  (success + s - 1) // s
            val = bisect_left(potions, min_s)
            res.append(n-val)
        return res
