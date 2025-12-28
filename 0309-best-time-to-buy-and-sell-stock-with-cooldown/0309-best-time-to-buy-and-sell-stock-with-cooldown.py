class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(i, flag):
            if (i, flag) in memo:
                return memo[(i, flag)]
            if i >= n:
                return 0
            if flag:
                buy = -prices[i] + dfs(i+1, 0)
                skip = dfs(i+1, 1)
                memo[(i, flag)] = max(buy, skip)
            else:
                sell = prices[i] + dfs(i+2, 1)
                skip = dfs(i+1, 0)
                memo[(i, flag)] = max(sell, skip)
            return memo[(i, flag)]
        
        return dfs(0, 1)
