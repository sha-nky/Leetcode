class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(numbers, i, j, target):
            pairs = []
            while j > i:
                s = numbers[i] + numbers[j]
                if s == target:
                    pairs.append([numbers[i], numbers[j]])
                    i += 1
                    j -= 1
                    while i < j and numbers[i] == numbers[i-1]:
                        i += 1
                    while i < j and numbers[j] == numbers[j+1]:
                        j -= 1
                elif s > target:
                    j -= 1
                else:
                    i += 1
            return pairs
        
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            pairs = twoSum(nums, i+1, len(nums)-1, -nums[i])
            for p in pairs:
                res.append([nums[i]] + p)
        
        return res
