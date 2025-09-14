class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        
        if start_color == color:
            return image
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if image[i][j] != start_color:
                return
            
            image[i][j] = color
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        dfs(sr, sc)
        return image
                
