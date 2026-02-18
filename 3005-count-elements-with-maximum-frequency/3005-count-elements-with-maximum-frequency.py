class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        maxFreq = max(hashmap.values())
        count = 0
        for freq in hashmap.values():
            if freq == maxFreq:
                count += 1
        
        return count * maxFreq
