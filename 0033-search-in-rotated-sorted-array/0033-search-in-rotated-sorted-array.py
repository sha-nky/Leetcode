class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:
            mid = left + (right-left)//2
            
            if nums[mid]==target: return mid

            if nums[mid] >= nums[left]: #left side sorted hai
                if nums[left] <= target and target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else: # right side sorted hai
                if nums[mid] <= target and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return -1