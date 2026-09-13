class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")" : "(", "}" : "{", "]": "["}
        stack = []

        for char in s:
            if char in pair:
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0