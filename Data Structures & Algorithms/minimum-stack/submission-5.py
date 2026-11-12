class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        val, min_val = self.stack[-1]
        return val

    def getMin(self) -> int:
        return self.stack[-1][1]
