class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def isPalin(string):
            return string == string[::-1]

        def dfs(i, substring):
            if i == n:
                res.append(substring[:])
                return
            
            for j in range(i, n):
                sub = s[i:j+1]
                if isPalin(sub):
                    substring.append(sub)
                    dfs(j+1, substring)
                    substring.pop()
        
        dfs(0, [])
        return res
