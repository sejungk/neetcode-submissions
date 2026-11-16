class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        total = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    total += 4

                    if row and grid[row - 1][col]:
                        total -= 2
                    if col and grid[row][col - 1]:
                        total -= 2
        return total
