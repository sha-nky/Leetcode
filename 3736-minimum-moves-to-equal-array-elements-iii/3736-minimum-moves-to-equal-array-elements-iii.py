class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        res = 0

        for num in nums:
            res += m - num
        
        return res
