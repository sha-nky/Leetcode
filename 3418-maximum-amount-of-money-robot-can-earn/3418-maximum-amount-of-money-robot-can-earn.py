from collections import deque

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # m, n = len(coins), len(coins[0])
        # max_profit = [[[float("-inf")] * 3 for _ in range(n)] for _ in range(m)]
        # max_profit[0][0][0] = coins[0][0]

        # queue = deque([(0, 0, 0, coins[0][0])])

        # if coins[0][0] < 0:
        #     max_profit[0][0][1] = 0
        #     queue.append((0, 0, 1, 0))

        # while queue:
        #     i, j, k, profit = queue.popleft()

        #     for di, dj in [(1, 0), (0, 1)]:
        #         ni, nj = i+di, j+dj

        #         if ni >= m or nj >= n:
        #             continue
                
        #         curr = coins[ni][nj]

        #         new_profit = profit + curr
        #         if new_profit > max_profit[ni][nj][k]:
        #             max_profit[ni][nj][k] = new_profit
        #             queue.append((ni, nj, k, new_profit))
                
        #         if curr < 0 and k < 2:
        #             if profit > max_profit[ni][nj][k+1]:
        #                 max_profit[ni][nj][k+1] = profit
        #                 queue.append((ni, nj, k+1, profit))
        
        # return max(max_profit[m-1][n-1])


        m, n = len(coins), len(coins[0])
        dp = [[[float("-inf")] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == float("-inf"):
                        continue
                    
                    for di, dj in [(0, 1), (1, 0)]:
                        ni, nj = i + di, j + dj
                        if ni >= m or nj >= n:
                            continue
                        
                        curr = coins[ni][nj]

                        dp[ni][nj][k] = max(
                            dp[ni][nj][k],
                            dp[i][j][k] + curr
                        )

                        if curr < 0 and k < 2:
                            dp[ni][nj][k+1] = max(
                                dp[ni][nj][k+1],
                                dp[i][j][k]
                            )
        
        return max(dp[m-1][n-1])
