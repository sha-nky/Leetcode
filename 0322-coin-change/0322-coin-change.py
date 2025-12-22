class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def rec(i, amt):
            if (i, amt) in memo:
                return memo[(i, amt)]
            if amt == 0:
                return 0
            if i > n-1 or amt < 0:
                return float("inf")
            
            take = 1 + rec(i, amt - coins[i])
            nottake = rec(i+1, amt)
            memo[(i, amt)] = min(take, nottake)
            return memo[(i, amt)]
        
        res = rec(0, amount)
        return -1 if res == float("inf") else res
