class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for num in range(n):
            res ^= start + (num << 1)
        
        return res
