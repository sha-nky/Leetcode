class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(comb, open, close):
            if len(comb) == n+n:
                res.append(''.join(comb))
                return
            
            if open < n:
                comb.append("(")
                backtrack(comb, open+1, close)
                comb.pop()
            
            if close < open:
                comb.append(")")
                backtrack(comb, open, close+1)
                comb.pop()
            
        backtrack([], 0, 0)
        return res
