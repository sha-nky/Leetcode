class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        moves = 0

        def bfs(r, c):
            queue.append((r, c))
            grid[r][c] = -1

            while queue:
                row, col = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = -1
                        queue.append((nr, nc))
        
        for row in range(rows):
            if grid[row][0] == 1: bfs(row, 0)
            if grid[row][cols-1] == 1: bfs(row, cols-1)
        for col in range(cols):
            if grid[0][col] == 1: bfs(0, col)
            if grid[rows-1][col] == 1: bfs(rows-1, col)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    moves += 1

        return moves
