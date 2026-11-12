class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        queue = deque()
        for row in range(ROWS):
            if board[row][0] == "O":
                queue.append((row, 0))
                board[row][0] = "."
            if board[row][COLS - 1] == "O":
                queue.append((row, COLS - 1))
                board[row][COLS - 1] = "."

        for col in range(COLS):
            if board[0][col] == "O":
                queue.append((0, col))
                board[0][col] = "."
            if board[ROWS - 1][col] == "O":
                queue.append((ROWS - 1, col))
                board[ROWS - 1][col] = "."

        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()

            for nr, nc in neighbors:
                new_row = nr + row
                new_col = nc + col
                if (0 <= new_row  < ROWS and 
                    0 <= new_col < COLS and
                    board[new_row][new_col] == "O"
                ):
                    queue.append((new_row, new_col))
                    board[new_row][new_col] = "."

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == ".":
                    board[row][col] = "O"
                
