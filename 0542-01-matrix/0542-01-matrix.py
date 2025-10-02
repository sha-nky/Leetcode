class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        inf = m + n
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    top = mat[i-1][j] if i > 0 else inf
                    left = mat[i][j-1] if j > 0 else inf
                    mat[i][j] = 1 + min(top, left)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i+1][j] if i < n-1 else inf
                    right = mat[i][j+1] if j < j-1 else inf
                    mat[i][j] = min(mat[i][j], 1 + min(bottom, right))
        
        return mat
