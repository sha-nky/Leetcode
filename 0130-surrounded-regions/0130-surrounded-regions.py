class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = deque()

        def bfs(r, c):
            queue.append((r, c))
            board[r][c] = "S"

            while queue:
                row, col = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = row+dr, col+dc

                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        board[nr][nc] = "S"
                        queue.append((nr, nc))
        
        for row in range(rows):
            if board[row][0] == "O": bfs(row, 0)
            if board[row][cols-1] == "O": bfs(row, cols-1)
        for col in range(cols):
            if board[0][col] == "O": bfs(0, col)
            if board[rows-1][col] == "O": bfs(rows-1, col)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        
        return board
