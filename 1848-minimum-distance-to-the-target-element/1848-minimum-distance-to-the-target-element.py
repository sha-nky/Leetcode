class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        i = j = start
        
        while i >= 0 or j < n:
            if i >= 0 and nums[i] == target:
                return start - i
            if j < n and nums[j] == target:
                return j - start
            
            i -= 1
            j += 1
