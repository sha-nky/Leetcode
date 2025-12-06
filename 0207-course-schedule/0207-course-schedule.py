class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            graph[pre].append(curr)
        
        visit = [0] * numCourses

        def dfs(node):
            if visit[node] == 1:
                return False
            if visit[node] == 2:
                return True
            
            visit[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visit[node] = 2
            return True
        
        for i in range(numCourses):
            if visit[i] == 0 and not dfs(i):
                return False
        return True
