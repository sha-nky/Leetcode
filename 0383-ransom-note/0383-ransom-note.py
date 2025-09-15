class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        f1 = {}
        f2 = {}

        for char in ransomNote:
            if char not in f1:
                f1[char] = 1
            else:
                f1[char] += 1
        
        for char in magazine:
            if char not in f2:
                f2[char] = 1
            else:
                f2[char] += 1
        
        uniq = set(ransomNote)

        for char in uniq:
            if char not in f2 or f1[char] > f2[char]:
                return False
        return True
