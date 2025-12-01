class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        n = len(nums)
        used = [False] * n

        def rec(temp):
            if len(temp) == n:
                res.append(temp[:])
                return
            
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    temp.append(nums[i])

                    rec(temp)

                    temp.pop()
                    used[i] = False
        
        rec([])
        return res
