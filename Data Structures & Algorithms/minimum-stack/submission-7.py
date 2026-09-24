class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        newVal = [val, min(val, self.stack[-1][1]) if self.stack else val]
        self.stack.append(newVal)
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
