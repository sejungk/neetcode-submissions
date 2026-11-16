class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        visited = set()
        def explore(row, col):
            
            if (row, col) in visited:
                return 0

            visited.add((row, col))
            
            perimeter = 4
            for nr, nc in neighbors:
                new_row = nr + row
                new_col = nc + col
                if (0 <= new_row < ROWS and 0 <= new_col < COLS and
                    grid[new_row][new_col] == 1
                    ):
                    perimeter -= 1
                    perimeter += explore(new_row, new_col)
            
            return perimeter

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return explore(row, col)

