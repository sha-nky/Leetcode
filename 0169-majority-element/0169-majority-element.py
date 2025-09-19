from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        for num in freq.keys():
            if freq.get(num) > (len(nums)//2):
                return num
