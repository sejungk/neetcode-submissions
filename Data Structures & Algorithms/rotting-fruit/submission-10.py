class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()
        minutes = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        def is_valid_fresh_fruit(row, col):
            return (
                0 <= row < ROWS and
                0 <= col < COLS and
                grid[row][col] == 1
            )

        while queue:
            row, col, curr_min = queue.popleft()
            minutes = curr_min
            
            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col
                if is_valid_fresh_fruit(new_row, new_col):                
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
                    queue.append((row + dr, col + dc, curr_min + 1))
        
        if fresh_count > 0:
            return -1
        return minutes
            
