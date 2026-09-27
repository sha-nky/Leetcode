class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = ""
        n = len(s)
        
        brackets = [0] * n
        stack = res = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                j = stack.pop()
                brackets[i] = j
                brackets[j] = i
        
        direction, i = 1, 0
        while i < n:
            if s[i].isalpha():
                res.append(s[i])
            else:
                i = brackets[i]
                direction = -direction
            
            i += direction
        
        return "".join(res)
