class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        n = ""
        possibleNines, remaining = divmod(sum, 9)

        while num:
            if possibleNines:
                if possibleNines == num:
                    if remaining:
                        return ""
                    else:
                        n += str(9)
                        possibleNines -= 1
                elif possibleNines > num:
                    return ""
                else:
                    n += str(9)
                    possibleNines -= 1
            else:
                n += str(remaining)
                remaining = 0

            num -= 1
        
        return n
