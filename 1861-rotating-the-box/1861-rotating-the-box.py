class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        rotatedBox = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                rotatedBox[i][j] = boxGrid[m - 1 - j][i]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if rotatedBox[i][j] == ".":
                    for k in range(i-1, -1, -1):
                        if rotatedBox[k][j] == "*":
                            break
                        elif rotatedBox[k][j] == ".":
                            continue
                        else:
                            rotatedBox[k][j], rotatedBox[i][j] = rotatedBox[i][j], rotatedBox[k][j]
        
        return rotatedBox
