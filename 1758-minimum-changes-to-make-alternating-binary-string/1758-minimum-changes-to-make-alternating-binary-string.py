class Solution:
    def minOperations(self, s: str) -> int:
        # n = len(s)
        # flag = 1
        # low, high = "", ""
        # for _ in range(n):
        #     low += "0" if flag else "1"
        #     high += "1" if flag else "0"
        #     flag = not flag
        
        # if s == low or s == high:
        #     return 0

        # c1, c2 = 0, 0
        # for i in range(n):
        #     c1 += 1 if s[i] != low[i] else 0
        #     c2 += 1 if s[i] != high[i] else 0
        
        # return min(c1, c2)


        diff = 0
        n = len(s)
        for i in range(n):
            if s[i] != ("1" if i % 2 == 0 else "0"):
                diff += 1
        
        return min(diff, n - diff)
