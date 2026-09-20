class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(1, n+1):
            res += i * (123 - ord(s[i-1]))
        
        return res
