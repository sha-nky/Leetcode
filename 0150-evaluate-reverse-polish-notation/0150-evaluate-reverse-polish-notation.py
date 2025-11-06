class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # operators = "+-*/"
        
        # for token in tokens:
        #     if token.lstrip("-").isdigit():
        #         stack.append(int(token))
        #     elif token in operators:
        #         if len(stack) < 2:
        #             return
        #         arg2 = stack.pop()
        #         arg1 = stack.pop()
        #         if token == "/" and arg2 == 0:
        #             return
        #         res = int(eval(str(arg1) + token + str(arg2)))
        #         stack.append(res)
        #     else:
        #         return
        
        # return stack.pop()


        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        
        return stack[0]
