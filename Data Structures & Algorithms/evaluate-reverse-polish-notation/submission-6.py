class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                i = stack.pop()
                stack[-1] = stack[-1] + i
            elif token == "-":
                i = stack.pop()
                stack[-1] = stack[-1] - i
            elif token == "*":
                i = stack.pop()
                stack[-1] = stack[-1] * i
            elif token == "/":
                i = stack.pop()
                stack[-1] = int(stack[-1] / i)
            else:
                stack.append(int(token))
        return stack[-1]