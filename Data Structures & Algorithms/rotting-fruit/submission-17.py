class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        fresh = 0
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                if grid[row][col] == 1:
                    fresh += 1
        max_mins = 0
        while queue:
            row, col, mins = queue.popleft()
            max_mins = mins

            for nr, nc in neighbors:
                new_row = nr + row
                new_col = nc + col
                if (0 <= new_row < ROWS and 0 <= new_col < COLS and
                    grid[new_row][new_col] == 1
                ):
                    fresh -= 1
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, mins + 1))
        
        return max_mins if fresh == 0 else -1