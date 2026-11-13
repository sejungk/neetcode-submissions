class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num2 - num1)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(float(num2) / num1))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]
