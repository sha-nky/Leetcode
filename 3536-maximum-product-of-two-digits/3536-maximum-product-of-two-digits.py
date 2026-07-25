class Solution:
    def maxProduct(self, n: int) -> int:
        # first, second = 0, 0

        # while n:
        #     dig = n % 10
        #     n //= 10

        #     if dig >= first:
        #         second = first
        #         first = dig
        #     elif dig >= second:
        #         second = dig
            
        # return first * second


        first, second = sorted(str(n))[-2:]
        return int(first) * int(second)
