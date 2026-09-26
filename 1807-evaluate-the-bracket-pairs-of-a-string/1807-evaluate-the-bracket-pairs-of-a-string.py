class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = {key: value for key, value in knowledge}
        
        res = []
        n = len(s)
        flag = 0

        for i in range(n):
            if s[i] == "(":
                flag = 1
                key = ""
            elif s[i] == ")":
                flag = 0
                res.append(knowledge.get(key, "?"))
                key = ""
            else:
                if flag:
                    key += s[i]
                else:
                    res.append(s[i])
        
        return "".join(res)
