class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(numbers, i, j, target):
            while j > i:
                if numbers[i] + numbers[j] == target:
                    return [numbers[i], numbers[j]]
                elif numbers[i] + numbers[j] > target:
                    j -= 1
                else:
                    i += 1
            return []
        
        res = []
        for i in range(0, len(nums)-3):
            res.append([nums[i]] + twoSum(nums, i+1, len(nums)-1, -nums[i]))
        return res
  