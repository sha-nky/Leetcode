class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        count = 0
        smallerNums = 0

        for num in nums:
            if num == target:
                count += 1
            elif num < target:
                smallerNums += 1
        
        while count:
            res.append(smallerNums)
            smallerNums += 1
            count -= 1
        
        return res
