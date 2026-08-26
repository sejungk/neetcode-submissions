class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def visit_island(grid, row, col, visited):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if ((row, col)) in visited:
                return
            if grid[row][col] == "0":
                return
            visited.add((row, col))
            visit_island(grid, row-1, col, visited)
            visit_island(grid, row, col+1, visited)
            visit_island(grid, row+1, col, visited)
            visit_island(grid, row, col-1, visited)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                item = grid[row][col]
                if (row, col) in visited:
                    continue
                if item == "1":
                    visit_island(grid, row, col, visited)
                    count+=1
        return count

        