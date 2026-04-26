class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [False] * (m * n)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c, pr, pc):
            visited[r * n + c] = True

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if (nr, nc) != (pr, pc):
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == grid[r][c]:
                            if visited[nr * n + nc] or dfs(nr, nc, r, c):
                                return True
            
            return False
        
        return any(not visited[i] and dfs(i // n, i % n, -1, -1) for i in range(m*n))
