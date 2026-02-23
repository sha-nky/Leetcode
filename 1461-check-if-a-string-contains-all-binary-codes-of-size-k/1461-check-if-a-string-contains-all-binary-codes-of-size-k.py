class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        i = 0
        substrings = set()
        while i < n - k + 1:
            substrings.add(s[i:i+k])
            i += 1
        
        return True if len(substrings) == 2**k else False
