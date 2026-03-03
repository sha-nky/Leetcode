class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        inter = set(nums1).intersection(nums2)
        min1, min2 = min(nums1), min(nums2)

        if len(inter) > 0:
            return min(inter)
        
        if min1 < min2:
            return min1*10 + min2
        return min2*10 + min1
