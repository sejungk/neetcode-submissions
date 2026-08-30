class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def dfs(row, col):
            if (row, col) in visited:
                return 0

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0

            if grid[row][col] == 0:
                return 0

            visited.add((row, col))

            return (1 + 
            dfs(row + 1, col) + 
            dfs(row, col + 1) +
            dfs(row - 1, col) +
            dfs(row, col - 1))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_area = max(max_area, dfs(row, col))

        return max_area