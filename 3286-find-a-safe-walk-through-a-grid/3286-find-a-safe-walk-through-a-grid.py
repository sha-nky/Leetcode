from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # m, n = len(grid), len(grid[0])
        # visited = set()

        # def dfs(i, j, h):
        #     if i < 0 or i >= m or j < 0 or j >= n:
        #         return False
            
        #     h -= grid[i][j]
        #     if h <= 0:
        #         return False
            
        #     if (i, j) == (m-1, n-1):
        #         return True
            
        #     if (i, j, h) in visited:
        #         return False
        #     visited.add((i, j, h))

        #     return (
        #         dfs(i+1, j, h) or
        #         dfs(i-1, j, h) or
        #         dfs(i, j+1, h) or
        #         dfs(i, j-1, h)
        #     )
        
        # return dfs(0, 0, health)


        m, n = len(grid), len(grid[0])

        init_health = health - grid[0][0]
        if init_health <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = init_health

        queue = deque([(0, 0, init_health)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y, h = queue.popleft()

            if (x, y) == (m-1, n-1):
                return True

            for dx, dy in directions:
                nx, ny = x+dx, y+dy

                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]

                    if nh <= 0:
                        continue

                    if nh > best[nx][ny]:
                        best[nx][ny] = nh
                        queue.append((nx, ny, nh))

        return False
