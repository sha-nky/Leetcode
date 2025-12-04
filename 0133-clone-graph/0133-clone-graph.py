"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # hashmap = {}
        # hashmap[node] = Node(node.val)
        # queue = deque([node])

        # while queue:
        #     cur = queue.pop()

        #     for neighbor in cur.neighbors:
        #         if neighbor not in hashmap:
        #             hashmap[neighbor] = Node(neighbor.val)
        #             queue.append(neighbor)
        #         hashmap[cur].neighbors.append(hashmap[neighbor])
        # return hashmap[node]


        hashmap = {}
        def dfs(cur):
            if cur in hashmap:
                return hashmap[cur]
            
            clone = Node(cur.val)
            hashmap[cur] = clone

            for neighbor in cur.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        return dfs(node)
