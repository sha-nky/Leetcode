class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        tar = sum(nums) - x

        if tar < 0: return -1
        if tar == 0: return n

        left = 0
        tot = 0
        longest = -1

        for right in range(n):
            tot += nums[right]
            while left <= right and tot > tar:
                tot -= nums[left]
                left += 1
            
            if tot == tar:
                longest = max(longest, right - left + 1)
            
        return -1 if longest == -1 else n - longest
