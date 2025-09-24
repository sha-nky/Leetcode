class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            weight += n % 2
            n = n >> 1
        
        return weight
