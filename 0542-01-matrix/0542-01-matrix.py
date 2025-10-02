class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # m, n = len(mat), len(mat[0])
        # inf = m + n
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] != 0:
        #             top = mat[i-1][j] if i > 0 else inf
        #             left = mat[i][j-1] if j > 0 else inf
        #             mat[i][j] = 1 + min(top, left)
        
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if mat[i][j] != 0:
        #             bottom = mat[i+1][j] if i < m-1 else inf
        #             right = mat[i][j+1] if j < n-1 else inf
        #             mat[i][j] = min(mat[i][j], 1 + min(bottom, right))
        
        # return mat

        rows, cols = len(mat), len(mat[0])
        queue = deque()

        rec = [[-1] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    rec[row][col] = 0
                    queue.append((row, col))
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rec[nr][nc] == -1:
                    rec[nr][nc] = rec[r][c] + 1
                    queue.append((nr, nc))
        
        return rec
