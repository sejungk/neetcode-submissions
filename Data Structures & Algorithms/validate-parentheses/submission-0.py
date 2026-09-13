class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")" : "(", "}" : "{", "]": "["}
        stack = []

        for char in s:
            if stack and char in pair and stack[-1] == pair[char]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0