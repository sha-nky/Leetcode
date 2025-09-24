class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def is_common_prefix(length):
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        left, right = 0, min(len(s) for s in strs)
        while left <= right:
            mid = left + (right-left)//2
            if is_common_prefix(mid):
                left = mid+1
            else:
                right = mid-1
        
        return strs[0][:right]
