class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = element = 0
        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count = 1
            elif nums[i] == element: count += 1
            else: count -= 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == element: count += 1
        if count > len(nums)//2: return element
        return -1