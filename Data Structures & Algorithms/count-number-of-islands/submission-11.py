class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()
        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False

            if (row, col) in visited:
                return False
            
            if grid[row][col] == "0":
                return False

            visited.add((row, col))
            for dr, dc in directions:
                dfs(dr + row, dc + col)

            return True

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    count += dfs(row, col)
        
        return count