class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            elif token in operators:
                if len(stack) < 2:
                    return
                arg2 = stack.pop()
                arg1 = stack.pop()
                if token == "/" and arg2 == 0:
                    return
                res = int(eval(str(arg1) + token + str(arg2)))
                stack.append(res)
            else:
                return
        
        return stack.pop()
