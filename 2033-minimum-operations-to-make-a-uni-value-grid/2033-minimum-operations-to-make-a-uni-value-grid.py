class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []

        for row in grid:
            for v in row:
                arr.append(v)

        base = arr[0]
        for v in arr:
            if abs(v - base) % x != 0:
                return -1

        arr.sort()

        median = arr[len(arr)//2]

        ops = 0
        for v in arr:
            ops += abs(v - median) // x

        return ops
