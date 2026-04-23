from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # ans = []
        # n = len(nums)

        # for i in range(n):
        #     dist = 0
        #     for j in range(n):
        #         if i != j and nums[i] == nums[j]:
        #             dist += abs(i - j)
        #     ans.append(dist)
        
        # return ans


        n = len(nums)
        ans = [0] * n

        dic = defaultdict(list)
        for i in range(n):
            dic[nums[i]].append(i)

        for ids in dic.values():
            size = len(ids)
            pref = [0] * size
            pref[0] = ids[0]

            for i in range(1, size):
                pref[i] = pref[i-1] + ids[i]
            
            for i in range(size):
                left = right = 0
                if i > 0:
                    left = i * ids[i] - pref[i-1]
                
                if i < size - 1:
                    right = (pref[size - 1] - pref[i]) - (size - i - 1) * ids[i]
                
                ans[ids[i]] = left + right
        
        return ans
