class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            count = 0
            while stack and temperatures[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1] 
                stack.pop()
            stack.append(i)
        return res