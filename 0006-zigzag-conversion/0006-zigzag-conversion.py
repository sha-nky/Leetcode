class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pattern = [[] for _ in range(numRows)]
        i = 0
        flag = -1
        
        for ch in s:
            pattern[i].append(ch)
            if flag == -1 and i < numRows-1:
                i += 1
            elif flag == 1 and i > 0:
                i -= 1
            if i == 0 or i == numRows-1:
                flag = -flag
        
        result = ""
        for row in pattern:
            result += ''.join(row)

        return result
