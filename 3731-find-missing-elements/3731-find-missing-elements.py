class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = float("inf"), -float("inf")
        exists = [False] * 101

        for num in nums:
            left, right = min(left, num), max(right, num)
            exists[num] = True
        
        if n == right-left+1:
            return []
        
        res = []
        for num in range(left+1, right):
            if not exists[num]:
                res.append(num)
        
        return res
