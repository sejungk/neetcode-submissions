class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        border_cells = []
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            if (board[row][0]) == "O":
                border_cells.append((row, 0))
            if (board[row][COLS-1]) == "O":
                border_cells.append((row, COLS-1))
        
        for col in range(COLS):
            if (board[0][col]) == "O":
                border_cells.append((0, col))
            if (board[ROWS-1][col]) == "O":
                border_cells.append((ROWS-1, col))

        queue = deque(border_cells)
        def bfs(letter):
            while queue:
                row, col = queue.popleft()
                board[row][col] = letter
  
                for dr, dc in directions:
                    new_row = dr + row
                    new_col = dc + col
                    if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                        continue
                    
                    if board[new_row][new_col] != "O":
                        continue
                
                    queue.append((new_row, new_col))

        bfs("1")

        for row in range(1, ROWS-1):
            for col in range(1, COLS-1):
                if board[row][col] == "O":
                    queue.append((row, col))
        
        bfs("X")
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "1":
                    board[row][col] = "O"