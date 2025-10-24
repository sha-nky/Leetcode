class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count_zeroes = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                count_zeroes += 1
        
        answer = []
        for num in nums:
            if count_zeroes > 1:
                answer.append(0)
            elif count_zeroes == 1:
                if num != 0:
                    answer.append(0)
                else:
                    answer.append(prod)
            else:
                answer.append(prod // num)

        return answer
