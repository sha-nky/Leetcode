class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        temp = [row[:] for row in mat]
        k = k % n

        for _ in range(k):
            for i in range(m):
                row = mat[i]

                if i % 2 == 0:
                    mat[i] = row[1:] + [row[0]]
                else:
                    mat[i] = [row[-1]] + row[:-1]
        
        return temp == mat
