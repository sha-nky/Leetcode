class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = []

        for char in s:
            if char == "(":
                if count>0:
                    res.append(char)
                count += 1

            if char==")":
                count -= 1
                if count>0:
                    res.append(char)

        return ''.join(res)
