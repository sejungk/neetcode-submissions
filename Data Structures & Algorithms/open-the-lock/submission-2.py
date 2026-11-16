class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set(deadends)
        queue = deque([("0000", 0)]) # curr code, turns
        visited = set(["0000"])

        while queue:
            code, count = queue.popleft()

            if code in ends:
                continue
            
            if code == target:
                return count

            for i in range(len(code)):

                up_char = (int(code[i]) + 1) % 10
                up = code[:i] + str(up_char) + code[i + 1:]

                down_char = (int(code[i]) - 1) % 10
                down = code[:i] + str(down_char) + code[i + 1:]

                for new_code in (up, down):
                    if new_code not in visited and new_code not in ends:
                        visited.add(new_code)
                        queue.append((new_code, count + 1))
        return -1

 