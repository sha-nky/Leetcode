class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        stack = []

        for char in s:
            freq[char] -= 1
            if char in seen:
                continue

            while stack and stack[-1] > char and freq[stack[-1]]:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)
