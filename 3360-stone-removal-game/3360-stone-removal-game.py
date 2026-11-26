class Solution:
    def canAliceWin(self, n: int) -> bool:
        flag = True
        for rem in range(10, 0, -1):
            if n < rem:
                return not flag
            n -= rem
            flag = not flag
