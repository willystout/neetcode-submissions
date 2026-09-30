class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            
            if token == "+":
                i = int(stack.pop())
                stack[-1] = int(stack[-1]) + i
            elif token == "-":
                i = int(stack.pop())
                stack[-1] = int(stack[-1]) - i
            elif token == "*":
                i = int(stack.pop())
                stack[-1] = int(stack[-1]) * i
            elif token == "/":
                i = int(stack.pop())
                stack[-1] = int(stack[-1]) / i
            else:
                stack.append(token)
        return int(stack[-1])