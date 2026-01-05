class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        INT_MAX = 2**31 -1
        
        if x < 0:
            flag = -1
            x = -x
        
        while x != 0:
            digit = x % 10
            x //= 10

            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit
        
        return rev * flag
