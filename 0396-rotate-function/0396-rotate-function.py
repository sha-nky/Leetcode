class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # n = len(nums)

        # if n == 1:
        #     return 0
        # if n == 2:
        #     return sum(nums)
        
        # maxValue = float("-inf")
        # for i in range(n):
        #     curr = 0
            
        #     for num, idx in enumerate(nums):
        #         curr += num * idx
            
        #     maxValue = max(maxValue, curr)
        #     nums = nums[-1:] + nums[:n-1]
        
        # return maxValue


        n = len(nums)
        F = 0
        maxValue = float("-inf")
        total = 0

        for i in range(n):
            total += nums[i]
            F += i * nums[i]
        
        maxValue = F
        for i in range(1, n):
            F += total - n * nums[-i]
            maxValue = max(maxValue, F)
        
        return maxValue
