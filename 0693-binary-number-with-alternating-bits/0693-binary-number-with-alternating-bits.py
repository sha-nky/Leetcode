class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n >>= 1
        while n:
            lsb = n & 1
            n >>= 1
            if lsb == prev:
                return False
            prev = lsb
        
        return True
