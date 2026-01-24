class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        nums.sort()
        minMaxPairSum = -float("inf")

        i, j = 0, len(nums)-1
        while i < j:
            minMaxPairSum = max(minMaxPairSum, nums[i] + nums[j])
            i += 1
            j -= 1
        
        return minMaxPairSum
