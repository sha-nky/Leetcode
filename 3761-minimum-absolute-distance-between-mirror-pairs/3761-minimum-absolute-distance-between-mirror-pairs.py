class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            return int(str(x)[::-1])
        
        n = len(nums)
        if n <= 1:
            return -1
        
        track = {}
        track[nums[-1]] = n - 1
        minDist = float("inf")

        for i in range(n-2, -1, -1):
            curr = reverse(nums[i])
            
            if curr in track:
                diff = abs(i - track[curr])
                minDist = min(minDist, diff)
            
            track[nums[i]] = i
        
        return -1 if minDist == float("inf") else minDist
