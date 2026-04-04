class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        l = len(encodedText)
        m, n = rows, l // rows
        matrix = [[" "] * n for _ in range(m)]
        
        i, j = 0, 0
        for k in range(l):
            matrix[i][j] = encodedText[k]
            j += 1
            if j == n:
                i += 1
                j = 0
        
        decodedText = ""
        for col in range(n):
            i, j = 0, col
            while i < m and j < n:
                decodedText += matrix[i][j]
                i += 1
                j += 1
        
        return decodedText.rstrip()
