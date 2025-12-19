class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def rec(n):
            if n<0:
                return 0
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = max(nums[n] + rec(n-2), rec(n-1))
            return dp[n]
        
        return rec(len(nums) - 1)
