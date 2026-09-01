class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific_pos = set()
        atlantic_pos = set()

        def bfs(source, ocean_pos):
            queue = deque(source)
            
            while queue:
                row, col = queue.popleft()
                ocean_pos.add((row, col))
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                        continue

                    if (new_row, new_col) in ocean_pos:
                        continue

                    if heights[new_row][new_col] < heights[row][col]:
                        continue

                    ocean_pos.add((new_row, new_col))
                    ocean_pos.add((new_row, new_col))

                    if 0 <= row < ROWS and 0 <= col < COLS:
                        curr_height = heights[row][col]
                    else:
                        curr_height = 0
                    queue.append((row + dr, col + dc))

        pacific = []
        atlantic = []
        for col in range(COLS):
            pacific.append((0, col))
            atlantic.append((ROWS-1, col))
        
        for row in range(ROWS):
            pacific.append((row, 0))
            atlantic.append((row, COLS-1))
        
        bfs(pacific, pacific_pos)
        bfs(atlantic, atlantic_pos)

        result = []
        for (row, col) in pacific_pos:
            if (row, col) in atlantic_pos:
                result.append((row, col))
        
        return result
