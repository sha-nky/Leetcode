class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1:------
        # if len(s)!=len(t):
        #     return False
        
        # track = [0] * 26
        
        # for i in range(len(s)):
        #     track[ord(s[i]) - ord("a")] += 1
        #     track[ord(t[i]) - ord("a")] -= 1
        
        # for count in track:
        #     if count != 0:
        #         return False
        
        # return True

        # Solution 2:------
        if len(s) != len(t):
            return False
        un = set(s)
        for char in s:
            if s.count(char) != t.count(char):
                return False
        
        return True
