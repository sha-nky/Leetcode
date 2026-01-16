class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        def allGaps(arr):
            s = set()
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    s.add(arr[j] - arr[i])
            return s

        hset = allGaps(h)
        vset = allGaps(v)

        common = hset & vset
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD
