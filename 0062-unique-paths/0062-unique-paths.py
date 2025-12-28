import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}

        # def rec(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if i == m-1 or j == n-1:
        #         return 1
        #     if i > m or j > n:
        #         return 0
            
        #     memo[(i, j)] = rec(i+1, j) + rec(i, j+1)
        #     return memo[(i, j)]
        
        # return rec(0, 0)


        # dp = [[1] * n for _ in range(m)]

        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1]


        return math.comb(m+n-2, m-1)
