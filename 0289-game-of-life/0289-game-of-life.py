class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return []
        
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), 
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for row in range(rows):
            for col in range(cols):
                count = 0
                for dx, dy in directions:
                    nrow, ncol = row+dx, col+dy
                    if (0 <= nrow < rows and 0 <= ncol < cols 
                        and abs(board[nrow][ncol]) == 1):
                        count += 1
                if board[row][col] == 1 and (count < 2 or count > 3):
                    board[row][col] = -1
                elif board[row][col] == 0 and count == 3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
