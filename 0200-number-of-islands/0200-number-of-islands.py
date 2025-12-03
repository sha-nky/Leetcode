class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited[r][c] = 1
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "1" and not visited[nr][nc]:
                            queue.append((nr, nc))
                            visited[nr][nc] = 1
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    count += 1
                    bfs(row, col)
        
        return count
