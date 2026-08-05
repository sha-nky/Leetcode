from collections import defaultdict

class Solution:
    def dfs(self, node, invoke, visited):
        visited[node] = 1
        for nxt in invoke[node]:
            if not visited[nxt]:
                self.dfs(nxt, invoke, visited)

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        invoke = defaultdict(list)

        for u, v in invocations:
            invoke[u].append(v)

        visited = [0] * n
        self.dfs(k, invoke, visited)

        remaining = []

        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))

        for i in range(n):
            if not visited[i]:
                remaining.append(i)

        return remaining
