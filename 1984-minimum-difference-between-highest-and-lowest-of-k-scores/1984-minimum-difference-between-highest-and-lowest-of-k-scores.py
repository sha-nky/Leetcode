class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        minDif = float("inf")

        for i in range(len(nums)-k+1):
            minDif = min(minDif, nums[i]-nums[i+k-1])
        
        return minDif
