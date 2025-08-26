class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        fc = any(matrix[i][0] == 0 for i in range(m))
        fr = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if fr:
            for i in range(n):
                matrix[0][i] = 0
            
        if fc:
            for j in range(m):
                matrix[j][0] = 0
        