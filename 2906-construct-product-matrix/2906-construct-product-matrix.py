class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        zeroes = 0
        tot_prod = 1
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeroes += 1
                else:
                    tot_prod *= grid[i][j]
        
        if zeroes > 1:
            return [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if zeroes == 1:
                    grid[i][j] = 0 if grid[i][j] != 0 else tot_prod % 12345
                    continue
                
                grid[i][j] = (tot_prod // grid[i][j]) % 12345
        
        return grid
