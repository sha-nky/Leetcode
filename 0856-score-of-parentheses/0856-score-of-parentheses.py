class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []

        for char in s:
            if char == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score << 1, 1)
        
        return score
