class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # Brute Force:-
        # res = []

        # def isAnagram(s1: str, s2: str) -> bool:
        #     if len(s1) != len(s2):
        #         return False
        #     track = [0] * 26
        #     for i in range(len(s1)):
        #         track[ord(s1[i]) - ord('a')] += 1
        #         track[ord(s2[i]) - ord('a')] -= 1
        #     for count in track:
        #         if count != 0:
        #             return False
        #     return True
        
        # visited = [0] * (len(strs))
        # for i in range(len(strs)):
        #     if not visited[i]:
        #         temp = [strs[i]]
        #         for j in range(i+1, len(strs)):
        #             if isAnagram(strs[i], strs[j]) and not visited[j]:
        #                 visited[j] = 1
        #                 temp.append(strs[j])
        #         res.append(temp)
        
        # return res


        # Optimized approach:-
        hashmap = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [word]
            else:
                hashmap[sorted_word].append(word)
        
        return list(hashmap.values())
