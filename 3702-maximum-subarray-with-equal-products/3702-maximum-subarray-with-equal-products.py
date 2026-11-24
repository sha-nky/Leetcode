class Solution:
    def maxLength(self, nums: List[int]) -> int:
        primes = {2, 3, 5, 7}
        def get_factors(x):
            return {p for p in primes if x % p == 0}
        
        n = len(nums)
        left = 0
        ans = min(n, 2)
        seen = set()
        
        for right in range(n):
            factors = get_factors(nums[right])
            while seen & factors:
                seen -= get_factors(nums[left])
                left += 1
            seen |= factors
            ans = max(ans, right - left + 1)
        
        return ans
