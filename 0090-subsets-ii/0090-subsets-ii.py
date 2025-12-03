class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        
        nums.sort()
        res = []
        n = len(nums)
        
        def rec(i, subset):
            if i == n:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            rec(i+1, subset)
            subset.pop()
            j = i
            while j+1 < n and nums[j] == nums[j+1]:
                j += 1
            rec(j+1, subset)
        
        rec(0, [])
        return res
