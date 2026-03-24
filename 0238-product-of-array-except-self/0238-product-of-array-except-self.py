class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # count_zeroes = 0
        # for num in nums:
        #     if num != 0:
        #         prod *= num
        #     else:
        #         count_zeroes += 1
        
        # answer = []
        # for num in nums:
        #     if count_zeroes > 1:
        #         answer.append(0)
        #     elif count_zeroes == 1:
        #         if num != 0:
        #             answer.append(0)
        #         else:
        #             answer.append(prod)
        #     else:
        #         answer.append(prod // num)

        # return answer


        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
