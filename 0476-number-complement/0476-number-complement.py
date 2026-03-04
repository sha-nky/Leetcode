class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        power = 0
        
        while num > 0:
            bit = num & 1
            flipped = 0 if bit else 1
            res |= (flipped << power)
            
            num >>= 1
            power += 1
        
        return res