class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        orgIdx = {}
        for i, key in enumerate(intervals):
            if tuple(key) not in orgIdx:
                orgIdx[tuple(key)] = i
        
        intervals = sorted(orgIdx.keys())
        n = len(intervals)

        nxtIdx = [0] * n
        for i in range(n):
            l, r, w = intervals[i]
            nxtIdx[i] = bisect.bisect_right(intervals, (r, float("inf"), float("inf")))
        
        dp = {}
        def solve(i, k):
            if i == n or k == 0:
                return (0, [])
            if (i, k) in dp:
                return dp[(i, k)]

            notTake = solve(i + 1, k)

            l, r, w = intervals[i]
            takeScore, takeIdx = solve(nxtIdx[i], k - 1)
            takeScore -= w
            takeIdx = sorted(takeIdx + [orgIdx[(l, r, w)]])
            take = (takeScore, takeIdx)

            res = min(take, notTake)
            dp[(i, k)] = res
            return res
        
        return solve(0, 4)[1]
