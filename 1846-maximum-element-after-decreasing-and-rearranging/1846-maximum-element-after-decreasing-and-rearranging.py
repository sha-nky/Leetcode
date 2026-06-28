class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # arr.sort()
        # n = len(arr)

        # arr[0] = 1
        # for i in range(1, n):
        #     arr[i] = min(arr[i], arr[i-1] + 1)
        
        # return arr[-1]


        n = len(arr)
        freq = [0] * (n + 1)

        for num in arr:
            freq[min(num, n)] += 1
        
        res = 1
        for i in range(2, n+1):
            res = min(freq[i] + res, i)
        
        return res
