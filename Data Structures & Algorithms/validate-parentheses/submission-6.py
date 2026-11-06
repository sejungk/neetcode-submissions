class Solution:
    def isValid(self, s: str) -> bool:
        opens = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for i in range(len(s)):
            if s[i] not in opens:
                stack.append(s[i])
            else:
                if not stack or stack[-1] != opens[s[i]]:
                    return False
                
                stack.pop()

        return len(stack) == 0