class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        res = []
        pac = set()
        atl = set()
        def dfs(row, col, ocean, prev):
            if ((row, col) in ocean or 
                (row < 0 or row >= ROWS or col < 0 or col >= COLS) or 
                heights[row][col] < prev
            ):
                return 
            

            ocean.add((row, col))
            for nr, nc in neighbors:
                new_row = nr + row
                new_col = nc + col
                dfs(row + nr, col + nc, ocean, heights[row][col])
            

        for row in range(ROWS):
            dfs(row, 0, pac, -float("inf"))
            dfs(row, COLS - 1, atl, -float("inf"))

        for col in range(COLS):
            dfs(0, col, pac, -float("inf"))
            dfs(ROWS - 1, col, atl, -float("inf"))

        res = []
        for row, col in pac:
            if (row, col) in atl:
                res.append([row, col])
        
        return res