class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        if n == 2:
            return [arr]
        
        res = []
        minDif = float("inf")
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            if diff == minDif:
                res.append(arr[i:i+2])
            elif diff < minDif and diff > 0:
                minDif = diff
                res = [arr[i:i+2]]
        
        return res
