class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        def update_row_col(start_row, start_col):
            for row in range(ROWS):
                if matrix[row][start_col] != 0:
                    matrix[row][start_col] = float("inf")

            for col in range(COLS):
                if matrix[start_row][col] != 0:
                    matrix[start_row][col] = float("inf")

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    update_row_col(row, col)
                
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == float("inf"):
                    matrix[row][col] = 0
