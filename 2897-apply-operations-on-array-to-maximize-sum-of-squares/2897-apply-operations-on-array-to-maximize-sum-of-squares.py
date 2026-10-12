class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        ans = 0
        bits = [0] * 31
        MOD = 10**9 + 7

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    bits[bit] += 1

        for _ in range(k):
            num = 0
            for bit in range(31):
                if bits[bit] > 0:
                    num |= 1 << bit
                    bits[bit] -= 1
        
            ans += (num * num) % MOD
        
        return ans % MOD
