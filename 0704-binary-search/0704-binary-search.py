class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def dfs(left, right):
            if right < left:
                return -1
            mid =  left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return dfs(left, mid - 1)
            else:
                return dfs(mid + 1, right)
        
        return dfs(0, len(nums)-1)
