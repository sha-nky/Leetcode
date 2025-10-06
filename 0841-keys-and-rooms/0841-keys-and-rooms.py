class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = []

        def dfs(i):
            if i<0 or i>=n:
                return False
            if i in visited:
                return
            visited.append(i)
            for ind in rooms[i]:
                dfs(ind)
        
        dfs(0)
        return len(visited) == n
