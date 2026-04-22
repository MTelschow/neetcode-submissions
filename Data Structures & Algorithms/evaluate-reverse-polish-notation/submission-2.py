class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue

            if token == '+':
                stack.append(stack.pop(-2) + stack.pop())
            if token == '-':
                stack.append(stack.pop(-2) - stack.pop())
            if token == '*':
                stack.append(stack.pop(-2) * stack.pop())
            if token == '/':
                stack.append(int(stack.pop(-2) / stack.pop()))
        return stack[0]
        