class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = [[0] * cols for _ in range(rows)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited[r][c] = 1
            area = 1

            while queue:
                row, col = queue.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = row+dr, col+dc
                    if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc]:
                        if grid[nr][nc]:
                            visited[nr][nc] = 1
                            queue.append((nr, nc))
                            area += 1
            return area
        
        maxArea = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and not visited[row][col]:
                    area = bfs(row, col)
                    maxArea = max(area, maxArea)
        return maxArea
