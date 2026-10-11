class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        tot = 0
        i = 1
        n = len(nums)

        for num in nums:
            tot += nums[i-1] ** 2 if n % i == 0 else 0
            i += 1
        
        return tot
