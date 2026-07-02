class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j, h):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            h -= grid[i][j]
            if h <= 0:
                return False
            
            if (i, j) == (m-1, n-1):
                return True
            
            if (i, j, h) in visited:
                return False
            visited.add((i, j, h))

            return (
                dfs(i+1, j, h) or
                dfs(i-1, j, h) or
                dfs(i, j+1, h) or
                dfs(i, j-1, h)
            )
        
        return dfs(0, 0, health)
