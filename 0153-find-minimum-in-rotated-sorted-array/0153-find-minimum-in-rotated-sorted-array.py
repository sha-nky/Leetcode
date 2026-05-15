class Solution:
    def findMin(self, nums: List[int]) -> int:
        least = float("inf")
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            
            least = min(least, nums[mid])

            if nums[mid] >= nums[right]:
                left = mid+1
            else:
                right = mid
        
        return least
