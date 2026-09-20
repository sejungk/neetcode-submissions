class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = "+-*/"
        stack = []

        for token in tokens:
            result = token
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    result = (a + b)
                elif token == "-":
                    result = (a - b)
                elif token == "*":
                    result = (a * b)
                elif token == "/":
                    result = (a / b)
            stack.append(int(result))
                
        return stack[-1]