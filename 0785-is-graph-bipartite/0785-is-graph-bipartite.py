class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        setA = set()
        setB = set()
        flip = False
        queue = deque()
        visited = set()

        def bfs(node):
            nonlocal flip
            
            queue.append(node)
            visited.add(node)
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    setA.add(curr) if flip else setB.add(curr)
                    for neighbour in graph[curr]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
                flip = not flip

        for node in range(len(graph)):
            if node not in visited:
                bfs(node)
        
        for node in range(len(graph)):
            for neighbour in graph[node]:
                if ((node in setA and neighbour in setA) or 
                    (node in setB and neighbour in setB)):
                    return False
        return True
