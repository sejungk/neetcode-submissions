class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            area = 0

            while queue:
                row, col = queue.popleft()
                if (row, col) in visited:
                    continue

                if grid[row][col] == 0:
                    continue

                visited.add((row, col))
                area += 1
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    if row + dr >= 0 and row + dr < len(grid) and col + dc >= 0 and col + dc < len(grid[0]):
                        queue.append([row + dr, col + dc])
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_area = max(max_area, bfs(row, col))

        return max_area
