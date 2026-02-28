class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # res = ""
        # mod = 10**9 + 7
        # for num in range(1, n+1):
        #     res += bin(num)[2:]
        
        # return int(res, 2) % mod


        mod = 10**9 + 7
        ans = [0] * (10**5 + 1)
        res = 0
        for i in range(1, 18):
            for b in range(2**(i-1), min(2**i, len(ans))):
                res = ((res << i) | b) % mod
                ans[b] = res
        
        return ans[n]
