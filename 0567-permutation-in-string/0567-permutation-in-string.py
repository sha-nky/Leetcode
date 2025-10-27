class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        
        hash1 = {}
        hash2 = {}
        
        for i in s1:
            hash1[i] = hash1.get(i, 0) + 1

        left = 0
        for right in range(n2):
            hash2[s2[right]] = hash2.get(s2[right], 0) + 1

            if right - left + 1 > n1:
                hash2[s2[left]] -= 1
                if hash2[s2[left]] == 0:
                    del hash2[s2[left]]
                left += 1
            
            if hash1 == hash2:
                return True
        
        return False
