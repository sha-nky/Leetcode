class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        track = {}
        for i in range(m):
            track["r" + f"{i}"] = mat[i].count(1)
        
        j = 0
        while j < n:
            count = 0
            i = 0
            while i < m:
                if mat[i][j] == 1:
                    count += 1
                i += 1
            track["c" + f"{j}"] = count
            j += 1
        
        result = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and track["r"+f"{i}"] == 1 and track["c"+f"{j}"] == 1:
                    result += 1
        
        return result
