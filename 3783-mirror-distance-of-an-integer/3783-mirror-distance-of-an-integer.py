class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(x: int) -> int:
            return int(str(x)[::-1])
        
        return abs(n - reverse(n))
