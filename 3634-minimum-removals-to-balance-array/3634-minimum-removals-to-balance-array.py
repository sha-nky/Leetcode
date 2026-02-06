class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # n = len(nums)
        # if n in [0, 1]:
        #     return 0

        # def rec(i, j, count):
        #     if i < 0 or i > n-1:
        #         return 0
        #     if nums[j] <= nums[i] * k:
        #         return count
            
        #     return min(rec(i+1, j, count+1), rec(i, j-1, count+1))
        
        # return rec(0, n-1, 0)


        nums.sort()
        n = len(nums)
        if n < 2:
            return 0
        
        l = 0
        maxLen = 0
        
        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            maxLen = max(maxLen, r - l + 1)
        
        return n - maxLen
