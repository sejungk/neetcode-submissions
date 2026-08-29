class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        visited = set()

        def dfs(row, col):
            if (row, col) in visited:
                return 0
            
            if row < 0 or row >= n or col < 0 or col >= m:
                return 0

            if grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            return 1 + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col -1)
        
        for row in range(n):
            for col in range(m):
                max_area = max(max_area, dfs(row, col))
        
        return max_area
