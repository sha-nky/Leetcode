class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [num*num for num in nums]
        nums.sort()
        
        n = len(nums)
        lowerSum = sum(nums[:n//2])
        higherSum = sum(nums[n//2:])

        return higherSum - lowerSum
