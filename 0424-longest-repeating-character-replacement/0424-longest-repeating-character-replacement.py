class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        n = len(s)

        for i in range(n):
            hashMap = {}
            maxFreq = 0
            for j in range(i, n):
                hashMap[s[j]] = hashMap.get(s[j], 0) + 1
                maxFreq = max(maxFreq, hashMap[s[j]])

                changes = (j-i+1) - maxFreq
                if changes <= k:
                    maxLen = max(maxLen, j-i+1)
                else:
                    break

        return maxLen
