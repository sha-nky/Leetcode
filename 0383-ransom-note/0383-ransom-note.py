class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1st solution :-
        # if len(ransomNote) > len(magazine):
        #     return False
        # f1 = {}
        # f2 = {}

        # for char in ransomNote:
        #     if char not in f1:
        #         f1[char] = 1
        #     else:
        #         f1[char] += 1
        
        # for char in magazine:
        #     if char not in f2:
        #         f2[char] = 1
        #     else:
        #         f2[char] += 1
        
        # uniq = set(ransomNote)

        # for char in uniq:
        #     if char not in f2 or f1[char] > f2[char]:
        #         return False
        # return True


        # 2nd sloution :-
        # if len(ransomNote) > len(magazine):
        #     return False
        
        # freq = {}
        # for char in ransomNote:
        #     freq[char] = freq.get(char, 0) + 1
        
        # for char in magazine:
        #     if char in freq and freq[char] > 0:
        #         freq[char] -= 1
        
        # for value in freq.values():
        #     if value > 0:
        #         return False
        # return True

        # 3rd Solution :-
        if len(ransomNote) > len(magazine):
            return False
        freq = {}
        remaining = len(ransomNote)

        for char in ransomNote:
            freq[char] = freq.get(char, 0) + 1

        for char in magazine:
            if char in freq and freq[char] > 0:
                freq[char] -= 1
                remaining -= 1
                if remaining == 0:
                    return True
        return False
