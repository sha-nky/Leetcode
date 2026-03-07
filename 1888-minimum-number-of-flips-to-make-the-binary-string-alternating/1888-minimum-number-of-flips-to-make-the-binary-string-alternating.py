class Solution:
    def minFlips(self, s: str) -> int :
        # n = len(s)
        
        # even, odd = (n + 1) // 2, n // 2
        # x = s[::2].count('1') - s[1::2].count('1')
        # res = min(even - x, odd + x)

        # if n & 1:
        #     for char in s:
        #         x = 2 * (ord(char) & 1) - x
        #         res = min(res, even - x, odd + x)
        
        # return res


        n = len(s)
        s = s + s
        p1, p2 = "", ""
        for i in range(n << 1):
            if i & 1:
                p1 += "0"
                p2 += "1"
            else:
                p1 += "1"
                p2 += "0"
        
        res = float("inf")
        d1, d2 = 0, 0
        l = 0
        for r in range(n << 1):
            if s[r] != p1[r]:
                d1 += 1
            if s[r] != p2[r]:
                d2 += 1
            
            if (r - l + 1) > n:
                if s[l] != p1[l]:
                    d1 -= 1
                if s[l] != p2[l]:
                    d2 -= 1
                l += 1

            if (r - l + 1) == n:
                res = min(res, d1, d2)
        
        return res
