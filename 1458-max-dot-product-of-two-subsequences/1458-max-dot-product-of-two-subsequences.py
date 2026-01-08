class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def rec(i, j):
            if i == len(nums1) or j == len(nums2):
                return -inf
            
            take = nums1[i] * nums2[j] + max(0, rec(i+1, j+1))
            skip1 = rec(i+1, j)
            skip2 = rec(i, j+1)

            return max(take, skip1, skip2)
        
        return rec(0, 0)
