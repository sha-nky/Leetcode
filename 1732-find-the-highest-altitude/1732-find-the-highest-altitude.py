class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        prefix = [0]

        for g in gain:
            prefix.append(prefix[-1] + g)
            maxAlt = max(maxAlt, prefix[-1])
        
        return maxAlt
