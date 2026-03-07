class Solution:
    def minFlips(self, s: str) -> int :
        n = len(s)
        
        even, odd = (n + 1) // 2, n // 2
        x = s[::2].count('1') - s[1::2].count('1')
        res = min(even - x, odd + x)

        if n & 1:
            for char in s:
                x = 2 * (ord(char) & 1) - x
                res = min(res, even - x, odd + x)
        
        return res
