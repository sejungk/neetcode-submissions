class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            if (board[row][0]) == "O":
                queue.append((row, 0))
                board[row][0] = "1"
            if (board[row][COLS-1]) == "O":
                queue.append((row, COLS-1))
                board[row][COLS-1] = "1"
        
        for col in range(COLS):
            if (board[0][col]) == "O":
                queue.append((0, col))
                board[0][col] = "1"
            if (board[ROWS-1][col]) == "O":
                queue.append((ROWS-1, col))
                board[ROWS-1][col] = "1"

        while queue:
            row, col = queue.popleft()
        
            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col
                if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                    continue
                    
                if board[new_row][new_col] != "O":
                    continue
                    
                board[new_row][new_col] = "1"
                queue.append((new_row, new_col))
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "1":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"