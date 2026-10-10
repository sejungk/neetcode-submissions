class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        min_heap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        n = len(grid)
        m = len(grid[0])

        while min_heap:
            max_height, row, col = heapq.heappop(min_heap)
            
            if row == n-1 and col == m-1:
                return max_height

            pos = (row, col)

            if pos in visited:
                continue
            visited.add(pos)

            for nr, nc in directions:
                new_row = nr + row
                new_col = nc + col
                if (0 <= new_row < n and 0 <= new_col < m 
                    and (new_row, new_col) not in visited):
                    new_height = max(max_height, grid[new_row][new_col])
                    heapq.heappush(min_heap, [new_height, new_row, new_col])

        