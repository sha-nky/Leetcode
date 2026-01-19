class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def squareSum(row, col, size):
            total = 0
            for i in range(size):
                for j in range(size):
                    total += mat[row + i][col + j]
            return total

        maxSize = 0
        m, n = len(mat), len(mat[0])
        maxSide = min(m, n)
        for size in range(maxSide, 0, -1):
            for row in range(m - size + 1):
                for col in range(n - size + 1):
                    total = squareSum(row, col, size)
                    if total <= threshold:
                        maxSize = max(maxSize, size)
        
        return maxSize
