class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if not s or len(s)==1: return s

        max_substr = ""
        for i in range(len(s)):
           odd_palin = expand_from_center(i, i)
           even_palin = expand_from_center(i, i+1)
           if len(odd_palin)>len(max_substr): max_substr = odd_palin
           if len(even_palin)>len(max_substr): max_substr = even_palin
        
        return max_substr
