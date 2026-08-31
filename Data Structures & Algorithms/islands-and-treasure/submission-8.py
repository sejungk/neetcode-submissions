class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        visited = set()
        while queue:
            row, col, dist = queue.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            
            if grid[row][col] == -1:
                continue
            
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            grid[row][col] = dist
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for nr, nc in directions:
                queue.append((row + nr, col + nc, dist + 1))
                        
            