class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])
        queries = sorted((t, i) for i, t in enumerate(queries))
        count = [0] * (n+1)
        ans = [0] * len(queries)
        l = r = active = 0

        for t, i in queries:
            while r < len(logs) and logs[r][1] <= t:
                id = logs[r][0]
                count[id] += 1
                if count[id] == 1:
                    active += 1
                r += 1
            
            while l < r and logs[l][1] < t-x:
                id = logs[l][0]
                count[id] -= 1
                if count[id] == 0:
                    active -= 1
                l += 1
            
            ans[i] = n - active
        
        return ans
