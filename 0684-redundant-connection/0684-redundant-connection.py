class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            rU = find(u)
            rV = find(v)

            if rU == rV:
                return False
            
            parent[rV] = rU
            return True
        
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):
                return [u, v]
