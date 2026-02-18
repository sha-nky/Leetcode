class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if int(nums1[i]) == int(nums2[j]):
                i += 1
                j += 1
                continue
            elif int(nums1[i]) < int(nums2[j]):
                return -1
            else:
                return 1
        
        if i < len(nums1):
            while i < len(nums1):
                if int(nums1[i]) != 0:
                    return 1
                i += 1
        
        if j < len(nums2):
            while j < len(nums2):
                if int(nums2[j]) != 0:
                    return -1
                j += 1
        
        return 0
