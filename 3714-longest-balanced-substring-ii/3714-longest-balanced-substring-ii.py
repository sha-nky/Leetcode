class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        
        ans = 1
        length = 1
        
        for i in range(1, n):
            if s[i] == s[i-1]:
                length += 1
            else:
                ans = max(ans, length)
                length = 1
        
        ans = max(ans, length)
        
        ab, bc, ca, abc = {}, {}, {}, {}
        
        ab[(0, 0)] = -1
        bc[(0, 0)] = -1
        ca[(0, 0)] = -1
        abc[(0, 0)] = -1
        
        cnt = [0, 0, 0]
        
        for i, ch in enumerate(s):
            cnt[ord(ch) - 97] += 1
            A, B, C = cnt
            
            key = (B - A, C - A)
            if key in abc:
                ans = max(ans, i - abc[key])
            else:
                abc[key] = i
            
            key = (A - B, C)
            if key in ab:
                ans = max(ans, i - ab[key])
            else:
                ab[key] = i
            
            key = (B - C, A)
            if key in bc:
                ans = max(ans, i - bc[key])
            else:
                bc[key] = i
            
            key = (C - A, B)
            if key in ca:
                ans = max(ans, i - ca[key])
            else:
                ca[key] = i
        
        return ans
