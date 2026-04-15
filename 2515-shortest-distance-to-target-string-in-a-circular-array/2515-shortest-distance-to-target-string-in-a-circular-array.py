class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        
        n = len(words)
        left, right = (startIndex - 1 + n) % n, (startIndex + 1) % n
        jumps = 1
        
        while left != startIndex or right != startIndex:
            if words[left] == target or words[right] == target:
                return jumps
            
            left = (left - 1 + n) % n
            right = (right + 1) % n
            jumps += 1
        
        return -1
