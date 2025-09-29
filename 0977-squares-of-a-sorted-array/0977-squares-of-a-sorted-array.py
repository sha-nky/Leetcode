class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        pos = neg = []
        point = 0
        while point < len(nums) and nums[point] < 0:
            point += 1

        pos = nums[point:]
        neg = nums[:point][::-1]
        
        res = []
        i, j = 0, 0
        while i < len(pos) and j < len(neg):
            if pos[i] < abs(neg[j]):
                res.append(pos[i] ** 2)
                i += 1
            else:
                res.append(neg[j] ** 2)
                j += 1
        if i < len(pos):
            while i < len(pos):
                res.append(pos[i] ** 2)
                i += 1
        
        if j < len(neg):
            while j < len(neg):
                res.append(neg[j] ** 2)
                j += 1
        
        return res
