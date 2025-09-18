class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        maxLen = 0
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for count in freq.values():
            maxLen += (count // 2) * 2
        if maxLen < len(s):
            maxLen += 1
        
        return maxLen
