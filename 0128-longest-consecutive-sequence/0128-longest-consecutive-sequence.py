class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashset = set(nums)

        for num in nums:
            if (num - 1) not in hashset:
                length = 1
                while (num + length) in hashset:
                    length += 1
                longest = max(longest, length)
        
        return longest
