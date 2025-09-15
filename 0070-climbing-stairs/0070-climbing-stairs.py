class Solution(object):
    def climbStairs(self, n):
        # 1st Solution :-
        # memo = {}
        
        # def rec(n):
        #     if n in [1, 2, 3]:
        #         return n
        #     if n in memo:
        #         return memo[n]
            
        #     memo[n] = rec(n-1) + rec(n-2)
        #     return memo[n]
        
        # return rec(n)


        # 2nd Solution :-
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
