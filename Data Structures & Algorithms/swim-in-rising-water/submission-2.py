class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()
        max_height = 0
        while min_heap:
            height, row, col = heapq.heappop(min_heap)
            
            max_height = max(max_height, height)

            if row == ROWS - 1 and col == COLS - 1:
                return max_height

            for nr, nc in directions:
                new_row = nr + row
                new_col = nc + col
                if ((new_row, new_col) not in visited and
                    0 <= new_row < ROWS and 0 <= new_col < COLS
                ):
                    visited.add((new_row, new_col))
                    heapq.heappush(min_heap, (grid[new_row][new_col], new_row, new_col))
        

        