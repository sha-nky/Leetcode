class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0 and len(nums1) != 0 and n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
        
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
