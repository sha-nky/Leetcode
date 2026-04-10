class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minDist = float("inf")
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] == nums[j] == nums[k]:
                        minDist = min(minDist, abs(i-j) + abs(j-k) + abs(k-i))
        
        return minDist if minDist != float("inf") else -1
 