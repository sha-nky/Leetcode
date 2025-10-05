class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        maxLen = 0
        dp = [[0]*cols for _ in range(rows)]
        
        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]
            path = 1
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols or matrix[nr][nc]<=matrix[r][c]:
                    continue
                path = max(path, 1 + dfs(nr, nc))
            dp[r][c] = path
            return dp[r][c]
        
        for row in range(rows):
            for col in range(cols):
                maxLen = max(maxLen, dfs(row, col))
        
        return maxLen
