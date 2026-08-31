class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        queue = deque()
        minutes = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_count += 1

        while queue:
            row, col, curr_min = queue.popleft()
            minutes = curr_min

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                if grid[new_row][new_col] == 0 or grid[new_row][new_col] == 2:
                    continue
                grid[new_row][new_col] = 2
                fresh_count -= 1
                queue.append((row + dr, col + dc, curr_min + 1))
        
        if fresh_count > 0:
            return -1
        return minutes
            
