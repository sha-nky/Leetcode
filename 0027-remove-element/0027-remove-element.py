class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n-1):
            if nums[i] == val:
                for j in range(i+1, n):
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
        for v in nums:
            if v != val:
                count += 1

        return count
