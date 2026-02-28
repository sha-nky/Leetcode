class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        mod = 10**9 + 7
        for num in range(1, n+1):
            res += bin(num)[2:]
        
        return int(res, 2) % mod
