class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitSum(num):
            return sum(int(d) for d in str(num))

        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]

        arr.sort(key=lambda x: (digitSum(x[0]), x[0]))

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][1] == i:
                continue

            cycleSize = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][1]
                cycleSize += 1

            swaps += cycleSize - 1

        return swaps
