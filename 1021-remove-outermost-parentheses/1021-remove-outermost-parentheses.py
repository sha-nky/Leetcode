class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        final = ""
        for i in s:
            if i=="(":
                if count>0:
                    final += i
                count += 1
            if i==")":
                count -= 1
                if count>0:
                    final += i
        return final
