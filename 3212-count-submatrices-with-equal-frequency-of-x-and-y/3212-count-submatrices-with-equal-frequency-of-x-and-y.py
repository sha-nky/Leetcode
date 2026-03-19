class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        xcount = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "X":
                    grid[i][j] = 1
                    xcount[i][j] = 1
                elif grid[i][j] == "Y": grid[i][j] = -1
                else: grid[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                    xcount[i][j] += xcount[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                    xcount[i][j] += xcount[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                    xcount[i][j] -= xcount[i-1][j-1]
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and xcount[i][j] > 0: count += 1
        
        return count
