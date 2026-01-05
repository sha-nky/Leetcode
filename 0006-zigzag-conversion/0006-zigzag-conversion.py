class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        pattern = [[] for _ in range(numRows)]
        i = 0
        direction = -1
        
        for ch in s:
            pattern[i].append(ch)
            
            if i == 0 or i == numRows-1:
                direction = -direction
            
            i += direction
        
        result = ""
        for row in pattern:
            result += ''.join(row)

        return result
