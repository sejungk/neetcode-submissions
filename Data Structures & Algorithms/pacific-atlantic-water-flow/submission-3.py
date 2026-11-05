class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        res = []
        pac = set()
        atl = set()
        def dfs(row, col, ocean):
            if (row, col) in ocean:
                return 

            ocean.add((row, col))
            for nr, nc in neighbors:
                new_row = nr + row
                new_col = nc + col
                if (0 <= new_row < ROWS and 0 <= new_col < COLS):
                    if (heights[new_row][new_col] >= heights[row][col]):
                        dfs(row + nr, col + nc, ocean)
            

        for row in range(ROWS):
            dfs(row, 0, pac)
            dfs(row, COLS - 1, atl)

        for col in range(COLS):
            dfs(0, col, pac)
            dfs(ROWS - 1, col, atl)

        res = []
        for row, col in pac:
            if (row, col) in atl:
                res.append([row, col])
        
        return res