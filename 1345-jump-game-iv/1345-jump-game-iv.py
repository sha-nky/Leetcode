from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        same = defaultdict(list)
        for i, val in enumerate(arr):
            same[val].append(i)
        
        visited = set([0])
        queue = deque([(0, 0)])

        while queue:
            ind, moves = queue.popleft()
            if ind == n-1:
                return moves
            
            if ind-1 >= 0 and ind-1 not in visited:
                queue.append((ind-1, moves+1))
                visited.add(ind-1)
            
            if ind+1 < n and ind+1 not in visited:
                queue.append((ind+1, moves+1))
                visited.add(ind+1)
            
            for n_ind in same[arr[ind]]:
                if n_ind not in visited:
                    visited.add(n_ind)
                    queue.append((n_ind, moves+1))
            
            same[arr[ind]].clear()
        
        return -1
