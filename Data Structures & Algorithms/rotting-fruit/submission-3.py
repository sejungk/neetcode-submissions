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

        visited = set()
        while queue:
            row, col, curr_min = queue.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            
            if (row, col) in visited:
                continue
            
            if grid[row][col] == 0:
                continue

            visited.add((row, col))
            minutes = max(minutes, curr_min)
            if grid[row][col] == 1:
                fresh_count -= 1
            grid[row][col] = 2
            

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                queue.append((row + dr, col + dc, curr_min + 1))
        
        if fresh_count > 0 :
            return -1
        return minutes
            
