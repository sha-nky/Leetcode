class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            res = []
            for char in string:
                if char == "#":
                    if res:
                        res.pop()
                else:
                    res.append(char)
            return "".join(res)
        
        return build(s) == build(t)
