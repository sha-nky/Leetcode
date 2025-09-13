class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r):
            if l>r: return -1

            mid = l + (r-l)//2
            if nums[mid]==target: return mid
            elif nums[mid]>target: return bs(l, mid-1)
            else: return bs(mid+1, r)
            
        return bs(0, len(nums)-1)