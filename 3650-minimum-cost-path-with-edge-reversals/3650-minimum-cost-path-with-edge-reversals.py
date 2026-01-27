import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,2*w))
        
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0,0)]
        
        while pq:
            cost,u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            if u == n-1:
                return cost
            for v,c in graph[u]:
                if cost + c < dist[v]:
                    dist[v] = cost + c
                    heapq.heappush(pq,(dist[v],v))
        
        return -1
