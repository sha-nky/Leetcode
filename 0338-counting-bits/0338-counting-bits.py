class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(b):
            count = 0
            while b:
                count += b % 2
                b = b >> 1
            return count

        res = []
        for i in range(n+1):
            res.append(countOnes(i))
        
        return res
