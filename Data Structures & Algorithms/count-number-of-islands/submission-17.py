class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 

            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            for dr, dc in directions:
                dfs(dr + row, dc + col)

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1

        return count