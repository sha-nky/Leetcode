class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def rec(i, curAmt):
            if i > n-1:
                return curAmt
            if (i, curAmt) in memo:
                return memo[(i, curAmt)]
            take = rec(i+2, curAmt + nums[i])
            notTake = rec(i+1, curAmt)
            memo[(i, curAmt)] = max(take, notTake)
            return memo[(i, curAmt)]
        
        return rec(0, 0)
