class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        res = 0

        for num in nums:
            res += abs(num - m)
        
        return res
