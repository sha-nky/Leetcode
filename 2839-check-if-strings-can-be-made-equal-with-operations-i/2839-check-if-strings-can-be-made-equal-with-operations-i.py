class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # m, n = len(s1), len(s2)
        # s1, s2 = list(s1), list(s2)

        # for i in range(m-2):
        #     s1[i], s1[i+2] = s1[i+2], s1[i]
            
        #     for j in range(n-2):
        #         if ''.join(s1) == ''.join(s2):
        #             return True
        #         s2[j], s2[j+2] = s2[j+2], s2[j]
            
        #     if ''.join(s1) == ''.join(s2):
        #         return True
        
        # return False


        return (
            sorted(s1[::2]) == sorted(s2[::2])
            and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )
