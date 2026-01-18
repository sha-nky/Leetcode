class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # def rowSumCheck(size, startR, startC):
        #     sumCheck = sum(grid[startR][startC + i] for i in range(size))
        #     for row in range(1, size):
        #         total = 0
        #         for col in range(size):
        #             total += grid[startR + row][startC + col]
        #         if total != sumCheck:
        #             return -1
        #     return sumCheck
        
        # def colSumCheck(size, startR, startC):
        #     sumCheck = sum(grid[startR + i][startC] for i in range(size))
        #     for col in range(1, size):
        #         total = 0
        #         for row in range(size):
        #             total += grid[startR + row][startC + col]
        #         if total != sumCheck:
        #             return -1
        #     return sumCheck
        
        # def diagSumCheck(size, startR, startC):
        #     diagSum, antiDiagSum = 0, 0
        #     for i in range(size):
        #         diagSum += grid[startR + i][startC + i]
        #         antiDiagSum += grid[startR + i][startC + (size - 1 - i)]
        #     if diagSum != antiDiagSum:
        #         return -1
        #     return diagSum

        # m, n = len(grid), len(grid[0])
        # maxSize = min(m, n)
        # for size in range(maxSize, 1, -1):
        #     for row in range(m - size + 1):
        #         for col in range(n - size + 1):
        #             r = rowSumCheck(size, row, col)
        #             if r == -1:
        #                 continue

        #             c = colSumCheck(size, row, col)
        #             if c == -1:
        #                 continue

        #             d = diagSumCheck(size, row, col)
        #             if d == -1:
        #                 continue

        #             if r == c == d:
        #                 return size

        # return 1


        m, n = len(grid), len(grid[0])

        rowPref = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                rowPref[r][c + 1] = rowPref[r][c] + grid[r][c]

        colPref = [[0] * n for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                colPref[r + 1][c] = colPref[r][c] + grid[r][c]

        def rowSum(r, c, size):
            return rowPref[r][c + size] - rowPref[r][c]

        def colSum(r, c, size):
            return colPref[r + size][c] - colPref[r][c]

        maxSize = min(m, n)

        for size in range(maxSize, 1, -1):
            for r in range(m - size + 1):
                for c in range(n - size + 1):

                    target = rowSum(r, c, size)

                    ok = True
                    for i in range(size):
                        if rowSum(r + i, c, size) != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    for j in range(size):
                        if colSum(r, c + j, size) != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    diag = anti = 0
                    for i in range(size):
                        diag += grid[r + i][c + i]
                        anti += grid[r + i][c + (size - 1 - i)]

                    if diag == anti == target:
                        return size

        return 1
