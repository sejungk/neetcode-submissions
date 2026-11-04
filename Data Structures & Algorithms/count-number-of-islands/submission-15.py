class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()
        def bfs(row, col):
            queue = deque([(row, col)])

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = dr + row
                    new_col = dc + col
                    if (0 <= new_row < ROWS and 
                        0 <= new_col < COLS and 
                        (new_row, new_col) not in visited and
                        grid[new_row][new_col] == "1"
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            return 1

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row, col))
                    count += bfs(row, col)
        
        return count