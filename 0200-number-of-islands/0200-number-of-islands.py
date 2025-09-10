class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if grid[r][c]=="0" or visited[r][c]:
                return
            
            visited[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and not visited[r][c]:
                    count += 1
                    dfs(r, c)
        
        return count
