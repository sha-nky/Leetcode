class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = [0 for _ in range(len(isConnected))]

        def dfs(node):
            visited[node] = 1

            for neighbour in range(len(isConnected[node])):
                if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)
        
        for i in range(len(visited)):
            if visited[i] == 0:
                count += 1
                dfs(i)
        
        return count
