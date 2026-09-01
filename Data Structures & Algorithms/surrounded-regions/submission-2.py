class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 or row == ROWS-1 or col == 0 or col == COLS-1) and board[row][col] == "O":
                    queue.append((row, col))
                    board[row][col] = "1"

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and board[nr][nc] == "O":                    
                    board[nr][nc] = "1"
                    queue.append((nr, nc))
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "1":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"