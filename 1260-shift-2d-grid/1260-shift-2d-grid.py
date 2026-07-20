class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        N = m * n
        k = k % N
        if not grid or not k: return grid

        def move(i, j):
            while i < j:
                grid[i // n][i % n], grid[j // n][j % n] = grid[j // n][j % n], grid[i // n][i % n]
                i += 1
                j -= 1
        
        move(0, N - 1)
        move(0, k - 1)
        move(k, N - 1)

        return grid
