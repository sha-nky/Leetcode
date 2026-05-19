class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        p1, p2 = 0, 0

        while p1 < n and p2 < m:
            x, y = nums1[p1], nums2[p2]
            
            if x == y:
                return x
            
            if x < y:
                p1 += 1
            else:
                p2 += 1
        
        return -1
