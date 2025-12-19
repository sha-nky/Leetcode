class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def rob(start, end):
            memo = {}

            def rec(i):
                if i > end:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(nums[i] + rec(i+2), rec(i+1))
                return memo[i]
            
            return rec(start)
        
        return max(rob(0, n-2), rob(1, n-1))
