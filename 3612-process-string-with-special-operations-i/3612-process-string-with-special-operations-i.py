class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        
        for char in s:
            if char == "*":
                result = result[:-1]
            elif char == "%":
                result = result[::-1]
            elif char == "#":
                result += result
            else:
                result += char
        
        return result
