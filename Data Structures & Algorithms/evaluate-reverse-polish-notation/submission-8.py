class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                continue
            b = stack.pop()
            a = stack.pop()
            
            res = 0
            if token == "+": res = a + b
            if token == "-": res = a - b
            if token == "*": res = a * b
            if token == "/": res = int(a / b)
                
            stack.append(res)
        
        return stack[0]
        