class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        track = [0] * 26
        
        for i in range(len(s)):
            track[ord(s[i]) - ord("a")] += 1
            track[ord(t[i]) - ord("a")] -= 1
        
        for count in track:
            if count != 0:
                return False
        
        return True
