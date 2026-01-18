class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def rowSumCheck(size, startR, startC):
            sumCheck = sum(grid[startR][startC + i] for i in range(size))
            for row in range(1, size):
                total = 0
                for col in range(size):
                    total += grid[startR + row][startC + col]
                if total != sumCheck:
                    return -1
            return sumCheck
        
        def colSumCheck(size, startR, startC):
            sumCheck = sum(grid[startR + i][startC] for i in range(size))
            for col in range(1, size):
                total = 0
                for row in range(size):
                    total += grid[startR + row][startC + col]
                if total != sumCheck:
                    return -1
            return sumCheck
        
        def diagSumCheck(size, startR, startC):
            diagSum, antiDiagSum = 0, 0
            for i in range(size):
                diagSum += grid[startR + i][startC + i]
                antiDiagSum += grid[startR + i][startC + (size - 1 - i)]
            if diagSum != antiDiagSum:
                return -1
            return diagSum

        m, n = len(grid), len(grid[0])
        maxSize = min(m, n)
        for size in range(maxSize, 1, -1):
            for row in range(m - size + 1):
                for col in range(n - size + 1):
                    r = rowSumCheck(size, row, col)
                    if r == -1:
                        continue

                    c = colSumCheck(size, row, col)
                    if c == -1:
                        continue

                    d = diagSumCheck(size, row, col)
                    if d == -1:
                        continue

                    if r == c == d:
                        return size

        return 1
