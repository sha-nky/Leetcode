class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        
        def isNonDecreasing(arr):
            return all(arr[i] >= arr[i-1] for i in range(1, len(arr)))
        
        while not isNonDecreasing(nums):
            minSum = float("inf")
            idx = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < minSum:
                    minSum = s
                    idx = i
        
            nums[idx] = minSum
            nums.pop(idx + 1)
            
            ans += 1
        
        return ans
