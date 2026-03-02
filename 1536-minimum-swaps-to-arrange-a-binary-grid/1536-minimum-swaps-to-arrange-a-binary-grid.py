class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeroes = [0] * len(grid)
        for i in range(len(grid)):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    zeroes[i] += 1
                else:
                    break
        
        swaps = 0
        for i in range(n):
            j = i
            while j < n and zeroes[j] < n-i-1:
                j += 1
            if j == n:
                return -1
            while j > i:
                zeroes[j], zeroes[j-1] = zeroes[j-1], zeroes[j]
                j -= 1
                swaps += 1
        
        return swaps
