from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def lowerBound(arr, x):
            left, right = 0, len(arr)-1

            while left < right:
                mid = left + ((right - left) >> 1)

                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            
            return left

        track = defaultdict(list)
        n = len(nums)
        res = []

        for i, num in enumerate(nums):
            track[num].append(i)
        
        for query in queries:
            curr = nums[query]
            indices = track[curr]

            if len(indices) == 1:
                res.append(-1)
                continue
            
            pos = lowerBound(indices, query)

            left = indices[pos - 1] if pos > 0 else indices[-1]
            right = indices[pos + 1] if pos < len(indices) - 1 else indices[0]

            d1 = abs(query - left)
            d1 = min(d1, n - d1)
            d2 = abs(query - right)
            d2 = min(d2, n - d2)

            res.append(min(d1, d2))
        
        return res
