class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        if len(heights)==1 and len(heights[0])==1:
            return [[0, 0]]
        
        rows, cols = len(heights), len(heights[0])
        pacific = [[0] * cols for _ in range(rows)]
        atlantic = [[0] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        result = []
        
        def dfs(row, col, visited):
            visited[row][col] = 1
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if heights[nr][nc] >= heights[row][col]:
                        dfs(nr, nc, visited)
        
        for row in range(rows): dfs(row, 0, pacific)
        for col in range(cols): dfs(0, col, pacific)
        for row in range(rows): dfs(row, cols-1, atlantic)
        for col in range(cols): dfs(rows-1, col, atlantic)

        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])
        
        return result
