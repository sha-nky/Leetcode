class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # def rec(i):
        #     if i > n-1:
        #         return 0
        #     return cost[i] + min(rec(i+1), rec(i+2))

        # return min(rec(0), rec(1))]


        n = len(cost)
        memo = {}
        def rec(i):
            if i > n-1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(rec(i+1), rec(i+2))
            return memo[i]
        
        return min(rec(0), rec(1))
