class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n-k+1) for _ in range(m-k+1)]

        for i in range(m-k+1):
            for j in range(n-k+1):
                nums = set()
                for x in range(i, i+k):
                    for y in range(j, j+k):
                        nums.add(grid[x][y])
                
                nums = sorted(nums)
                if len(nums) <= 1:
                    res[i][j] = 0
                else:
                    res[i][j] = min(nums[x+1] - nums[x] for x in range(len(nums)-1))
        
        return res
