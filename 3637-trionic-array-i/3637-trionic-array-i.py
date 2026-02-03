class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        direction = 0

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return False
            
            if direction == 0:
                if nums[i] < nums[i+1]:
                    continue
                elif nums[i] > nums[i+1]:
                    if i == 0:
                        return False
                    direction = 1
                else:
                    return False
            
            elif direction == 1:
                if nums[i] > nums[i+1]:
                    continue
                elif nums[i] < nums[i+1]:
                    direction = 2
                else:
                    return False
            
            else:
                if nums[i] < nums[i+1]:
                    continue
                else:
                    return False
        
        return direction == 2
