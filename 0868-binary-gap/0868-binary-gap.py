class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        maxDistance = 0

        i = 0
        while i < len(binary):
            if binary[i] == "1":
                j = i+1

                while j < len(binary) and binary[j] != "1":
                    j += 1

                if j < len(binary):
                    maxDistance = max(maxDistance, j - i)
                i = j
            else:
                i += 1
        
        return maxDistance
