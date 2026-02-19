class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # tracks = []
        # left, right = 0, 0
        # while right < len(s):
        #     if s[right] == s[left]:
        #         right += 1
        #     else:
        #         tracks.append(right - left)
        #         left = right
        # tracks.append(right - left)
        
        # if len(tracks) in [0, 1]:
        #     return 0
        
        # count = 0
        # for i in range(len(tracks)-1):
        #     count += min(tracks[i], tracks[i+1])
        
        # return count


        count = 0
        cur, prev = 1, 0
        right = 1

        while right < len(s):
            if s[right] == s[right - 1]:
                cur += 1
            else:
                count += min(prev, cur)
                prev = cur
                cur = 1
            right += 1

        count += min(prev, cur)
        return count
