class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        min_suffix = [0] * n

        min_suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            min_suffix[i] = min(min_suffix[i+1], nums[i])
        
        max_prefix = nums[0]
        for i in range(n):
            max_prefix = max(max_prefix, nums[i])
            
            if max_prefix - min_suffix[i] <= k:
                return i
        
        return -1
