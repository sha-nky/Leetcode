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


        nums.sort()
        n = len(nums)

        return nums == list(range(1, n)) + [n-1]
