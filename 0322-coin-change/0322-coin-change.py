class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def rec(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float("inf")
            if amt in memo:
                return memo[amt]
            
            ans = float("inf")
            for coin in coins:
                ans = min(ans, 1 + rec(amt - coin))
            
            memo[amt] = ans
            return memo[amt]
        
        res = rec(amount)
        return -1 if res == float("inf") else res
