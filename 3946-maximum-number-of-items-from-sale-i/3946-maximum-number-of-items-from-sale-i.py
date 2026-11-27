class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        precomp = {}
        
        for i, (f_i, _) in enumerate(items):
            precomp[i] = [
                j for j, (f_j, _) in enumerate(items)
                if f_j % f_i == 0 and j != i
            ]
        
        min_price = min(price for _, price in items)
        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i, (_, price) in enumerate(items):
            value = 1 + len(precomp[i])

            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    dp[c] = max(dp[c], dp[c - price] + value)

        ans = 0
        for spent in range(budget + 1):
            if dp[spent] != -1:
                additional = (budget - spent) // min_price
                ans = max(ans, dp[spent] + additional)

        return ans
