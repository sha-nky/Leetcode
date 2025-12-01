class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n = 1 << (len(nums))
        # ans = []

        # for num in range(n):
        #     l = []
        #     for i in range(len(nums)):
        #         if num & (1 << i):
        #             l.append(nums[i])
        #     ans.append(l)
        
        # return ans


        res = []

        def rec(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            rec(i+1, subset)
            subset.pop()
            rec(i+1, subset)
        
        rec(0, [])
        return res
