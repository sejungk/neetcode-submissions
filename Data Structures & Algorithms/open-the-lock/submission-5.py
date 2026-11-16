class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set(deadends)
        visited = set(deadends)

        if "0000" in visited:
            return -1

        visited.add("0000")
        queue = deque([("0000")]) # code
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                code = queue.popleft()

                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(code[i]) + j + 10) % 10)
                        next_code = code[:i] + digit + code[i + 1:]

                        if next_code == target:
                            return count

                        if next_code not in visited:
                            visited.add(next_code)
                            queue.append(next_code)
        return -1

 