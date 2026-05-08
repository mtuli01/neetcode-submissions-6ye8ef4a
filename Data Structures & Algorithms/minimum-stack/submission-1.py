class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        if not self.stack and not self.min_stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
