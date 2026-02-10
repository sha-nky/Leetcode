class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            cnt = [0, 0]
            for j in range(i, n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    cnt[nums[j] % 2] += 1
                if cnt[0] == cnt[1]:
                    ans = max(ans, j - i + 1)
        return ans
