class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(row, col):
            queue = collections.deque()
            queue.append((row, col))
            while len(queue) > 0:
                row, col = queue.popleft()
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                if grid[row][col] == "0":
                    continue
                if (row, col) in visited:
                    continue

                queue.append((row+1, col))
                queue.append((row, col+1))
                queue.append((row-1, col))
                queue.append((row, col-1))
                visited.add((row, col))

        for row in range(rows):
            for col in range(cols):
                item = grid[row][col]
                if item == "1" and (row, col) not in visited:
                    bfs(row, col)
                    count += 1
        return count