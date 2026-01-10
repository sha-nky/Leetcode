class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        memo = {}
        
        def dfs(i, j):
            if i == m:
                return sum(ord(c) for c in s2[j:])
            if j == n:
                return sum(ord(c) for c in s1[i:])
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s1[i] == s2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                memo[(i, j)] = min(
                    ord(s1[i]) + dfs(i+1, j),
                    ord(s2[j]) + dfs(i, j+1)
                )
            return memo[(i, j)]
        
        return dfs(0, 0)
