class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        moves = 0

        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    moves += 1
        
        return moves + len(stack)
