class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dp = {}

        def dfs(row, col):
            if (row, col) in dp:
                return dp[(row, col)]

            max_path = 1
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col
                
                if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[row][col]):
                    max_path = max(max_path, 1 + dfs(nr, nc))

            dp[(row, col)] = max_path
            return max_path


        max_path = 0
        for row in range(rows):
            for col in range(cols):
                max_path = max(dfs(row, col), max_path)

        return max_path
        
