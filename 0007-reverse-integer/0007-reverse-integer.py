class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        
        rev = int(str(x)[::-1])

        if rev > 2**31 - 1:
            return 0
        
        return rev * flag
