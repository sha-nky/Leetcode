class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        rL = 1000

        while rL <= n:
            commas += n - rL + 1
            rL *= 1000
        
        return commas
