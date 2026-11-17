class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        min_heap = [(0, 0, 0)]
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
    
        while min_heap:
            height, row, col = heapq.heappop(min_heap)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == ROWS - 1 and col == COLS - 1:
                return height

            for nr, nc in neighbors:
                new_row = nr + row
                new_col = nc + col

                if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited:
                    new_height = max(height, abs(heights[row][col] - heights[new_row][new_col]))
                    heapq.heappush(min_heap, (new_height, new_row, new_col))
                    
        
