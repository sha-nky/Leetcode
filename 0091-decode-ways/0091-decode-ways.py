class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def rec(i):
            if i in memo:
                return memo[i]
            if i > n-1:
                return 1
            if s[i] == '0':
                return 0
            
            count = rec(i+1)

            if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                count += rec(i+2)
            
            memo[i] = count
            return memo[i]
        
        return rec(0)
