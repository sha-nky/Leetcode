class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        n, m = len(arr1), len(arr2)
        count = 0

        for i in range(n):
            flag = 1
            for j in range(m):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = 0
                    continue
            
            count += flag
        
        return count
