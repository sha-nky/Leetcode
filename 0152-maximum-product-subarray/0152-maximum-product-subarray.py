class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = mini = ans = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            temp = max(n, n*maxi, n*mini)
            mini = min(n, n*maxi, n*mini)
            maxi = temp
            ans = max(ans, maxi)
        
        return ans
