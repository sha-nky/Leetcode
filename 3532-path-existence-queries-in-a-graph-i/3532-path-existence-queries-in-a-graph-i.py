class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        compute = [0] * n

        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                compute[i] = compute[i-1]
            else:
                compute[i] = compute[i-1] + 1

        return [compute[u] == compute[v] for u, v in queries]
