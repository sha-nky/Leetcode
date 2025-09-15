class Solution(object):
    def climbStairs(self, n):
        memo = {}
        
        def rec(n):
            if n in [1, 2, 3]:
                return n
            if n in memo:
                return memo[n]
            
            memo[n] = rec(n-1) + rec(n-2)
            return memo[n]
        
        return rec(n)
