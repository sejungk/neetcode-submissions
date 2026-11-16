class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        total = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    peri = 4

                    for nr, nc in neighbors:
                        new_row = nr + row
                        new_col = nc + col
                        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                            if grid[new_row][new_col] == 1:
                                peri -= 1
                
                    total += peri
        return total
