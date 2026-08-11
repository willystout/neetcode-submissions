class MinStack:

    def __init__(self):
        self.minimum = []
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.minimum) == 0:
            self.minimum.append(val)
        else:
            self.minimum.append(min(self.minimum[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        if not len(self.minimum) == 0 or not len(self.stack.pop()) == 0:
            self.minimum.pop()
            self.stack.pop()

    def top(self) -> int:
        if not len(self.minimum) == 0 or not len(self.stack.pop()) == 0:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if not len(self.minimum) == 0 or not len(self.stack.pop()) == 0:
            return self.minimum[-1]
