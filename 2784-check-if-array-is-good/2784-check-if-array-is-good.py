class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # n = len(nums) - 1
        # if max(nums) != n:
        #     return False
        
        # if nums.count(n) != 2:
        #     return False
        
        # if len(set(nums)) != n:
        #     return False
        
        # return True



        # nums.sort()
        # n = len(nums)

        # return nums == list(range(1, n)) + [n-1]



        nums.sort()
        max_ele = nums[-1]
        if len(nums) != max_ele + 1 or nums[-1] != nums[-1-1]:
            return False
        
        for i in range(max_ele - 1):
            if nums[i] != i + 1:
                return False
        return True
