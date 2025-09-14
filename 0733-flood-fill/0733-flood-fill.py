class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        def dfs(i, j):
            if i == m or j == n:
                return
            if image[i][j] == color:
                return
            prev = image[i][j]
            image[i][j] = color
            if i+1 != m and image[i+1][j]==prev:
                dfs(i+1, j)
            if i-1 != -1 and image[i-1][j]==prev:
                dfs(i-1, j)
            if j-1 != -1 and image[i][j-1]==prev:
                dfs(i, j-1)
            if j+1 != n and image[i][j+1]==prev:
                dfs(i, j+1)
        
        dfs(sr, sc)
        return image
                
