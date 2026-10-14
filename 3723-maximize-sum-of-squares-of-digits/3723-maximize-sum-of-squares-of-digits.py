class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # n = ""
        # possibleNines, remaining = divmod(sum, 9)

        # while num:
        #     if possibleNines:
        #         if possibleNines == num:
        #             if remaining:
        #                 return ""
        #             else:
        #                 n += str(9)
        #                 possibleNines -= 1
        #         elif possibleNines > num:
        #             return ""
        #         else:
        #             n += str(9)
        #             possibleNines -= 1
        #     else:
        #         n += str(remaining)
        #         remaining = 0

        #     num -= 1
        
        # return n


        # n = []
        # possibleNines, remaining = divmod(sum, 9)

        # while num:
        #     if possibleNines:
        #         if possibleNines == num and remaining:
        #             return ""
        #         elif possibleNines > num:
        #             return ""

        #         n.append("9")
        #         possibleNines -= 1
        #     else:
        #         n.append(str(remaining))
        #         remaining = 0

        #     num -= 1
        
        # return "".join(n)


        if sum > 9 * num:
            return ""

        n = []
        possibleNines, remaining = divmod(sum, 9)

        while num:
            if possibleNines:
                n.append("9")
                possibleNines -= 1
            else:
                n.append(str(remaining))
                remaining = 0

            num -= 1

        return "".join(n)
