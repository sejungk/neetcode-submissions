class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()
        def dfs(row, col):  
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0

            if (row, col) in visited:
                return 0

            if grid[row][col] != 1:
                return 0
            
            visited.add((row, col))

            area = 1
            for nr, nc in neighbors:
                area += dfs(row + nr, col + nc)
            
            return area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area