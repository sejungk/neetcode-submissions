class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
 
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        while queue:
            row, col, dist = queue.popleft()
                
            for nr, nc in neighbors:
                new_row = row + nr
                new_col = col + nc
                if (0 <= new_row < ROWS and 0 <= new_col < COLS and
                    grid[new_row][new_col] == 2147483647
                ):
                    grid[new_row][new_col] = dist + 1
                    queue.append((new_row, new_col, dist + 1))