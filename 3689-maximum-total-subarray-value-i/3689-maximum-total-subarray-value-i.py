class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minNum = maxNum = nums[0]

        for num in nums:
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)

        return (maxNum - minNum) * k
