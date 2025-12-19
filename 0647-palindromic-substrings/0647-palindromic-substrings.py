class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalin(s):
            return s == s[::-1]
        
        n = len(s)
        count = 0
        for i in range(n):
            count += 1
            for j in range(i+1, n):
                if isPalin(s[i:j+1]):
                    count += 1
        
        return count
