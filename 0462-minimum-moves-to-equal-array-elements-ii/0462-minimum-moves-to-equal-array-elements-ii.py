class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        nums.sort()
        m = nums[n//2]
        res = 0

        for num in nums:
            res += abs(m - num)
        
        return res
