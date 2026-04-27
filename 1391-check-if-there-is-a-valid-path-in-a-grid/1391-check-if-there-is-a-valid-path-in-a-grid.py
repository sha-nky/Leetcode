class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # m, n = len(grid), len(grid[0])
        # allowed = {
        #     1: [(0, -1), (0, 1)],
        #     2: [(-1, 0), (1, 0)],
        #     3: [(1, 0), (0, -1)],
        #     4: [(1, 0), (0, 1)],
        #     5: [(-1, 0), (0, -1)],
        #     6: [(-1, 0), (0, 1)],
        # }

        # visited = set()

        # def dfs(i, j, visited):
        #     if (i, j) == (m-1, n-1):
        #         return True
            
        #     visited.add((i, j))
            
        #     for dx, dy in allowed[grid[i][j]]:
        #         ni, nj = i + dx, j + dy
                
        #         if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
        #             if (-dx, -dy) in allowed[grid[ni][nj]]:
        #                 if dfs(ni, nj, visited):
        #                     return True
            
        #     return False

        # return dfs(0, 0, visited)


        m, n = len(grid), len(grid[0])
        allowed = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)],
        }
        
        q = deque([(0, 0)])
        visited = {(0, 0)}
        
        while q:
            i, j = q.popleft()
            
            if (i, j) == (m - 1, n - 1):
                return True
            
            for dx, dy in allowed[grid[i][j]]:
                ni, nj = i + dx, j + dy
                
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    if (-dx, -dy) in allowed[grid[ni][nj]]:
                        visited.add((ni, nj))
                        q.append((ni, nj))
        
        return False
