class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # grid = [["#"] * n for _ in range(m)]
        # grid[0][0] = "."
        # i, j = 0, 0

        # while i < m-1 or j < n-1:
        #     if j < n-1:
        #         j += 1
        #         grid[i][j] = "."
            
        #     if i < m-1:
        #         i += 1
        #         grid[i][j] = "."
        
        # return ["".join(row) for row in grid]
        # # return list(map(lambda x:"".join(x), grid))


        grid = [["#"] * n for _ in range(m)]

        for j in range(n):
            grid[0][j] = "."
        
        for i in range(m):
            grid[i][n-1] = "."
        
        return ["".join(row) for row in grid]
