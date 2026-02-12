class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        
        for i in range(n):
            freq = [0] * 26
            distinct = 0
            maxFreq = 0
            
            for j in range(i, n):
                ind = ord(s[j]) - ord('a')
                
                if freq[ind] == 0:
                    distinct += 1
                
                freq[ind] += 1
                maxFreq = max(maxFreq, freq[ind])
                
                length = j - i + 1
                
                if length == distinct * maxFreq:
                    maxLen = max(maxLen, length)
        
        return maxLen
