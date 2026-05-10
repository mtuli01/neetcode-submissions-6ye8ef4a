class Solution:
    def calculate(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return int(a / b)  # truncate toward zero
        else:
            return 0

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b = stack.pop()  # second operand
                a = stack.pop()  # first operand
                stack.append(self.calculate(a, b, token))
            else:
                stack.append(int(token))

        return stack[0]