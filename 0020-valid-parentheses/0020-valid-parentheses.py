class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in mappings.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mappings[char]:
                    return False
                stack.pop()
        return not stack
