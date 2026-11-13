class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        stack = []
        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s

            if len(stack) >= 1 and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)
