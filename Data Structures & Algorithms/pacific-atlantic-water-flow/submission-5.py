class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        res = []
        pac = set()
        atl = set()
        def bfs(row, col, ocean):
            queue = deque([(row, col)])
            
            while queue:
                row, col = queue.popleft()
                ocean.add((row, col))
                
                for dr, dc in directions:
                    new_row = dr + row
                    new_col = dc + col
                    if (0 <= new_row < ROWS and 
                        0 <= new_col < COLS and 
                        (new_row, new_col) not in ocean and
                        heights[row][col] <= heights[new_row][new_col]
                    ):
                        queue.append((new_row, new_col)) 

        for row in range(ROWS):
            bfs(row, 0, pac)
            bfs(row, COLS - 1, atl)

        for col in range(COLS):
            bfs(0, col, pac)
            bfs(ROWS - 1, col, atl)

        res = []
        for row, col in pac:
            if (row, col) in atl:
                res.append([row, col])
        
        return res