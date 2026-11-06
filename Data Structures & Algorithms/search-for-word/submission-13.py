class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        n = len(word)

        def dfs(row, col, i):
            if i == (n - 1):
                return True
            
            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col
                if (0 <= new_row < ROWS and 0 <= new_col < COLS and
                    board[new_row][new_col] == word[i + 1]
                ):
                    char = board[row][col]
                    board[row][col] = "#"
                    if dfs(new_row, new_col, i + 1):
                        board[row][col] = char
                        return True

                    board[row][col] = char
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False