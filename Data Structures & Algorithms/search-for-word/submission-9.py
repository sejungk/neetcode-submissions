class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, i):
            nonlocal directions
            nonlocal n
            nonlocal m

            if i == len(word):
                return True

            if row < 0 or row >= n or col < 0 or col >= m:
                return False

            if word[i] != board[row][col]:
                return False

            curr_char = board[row][col]
            board[row][col] = ""
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if dfs(new_row, new_col, i + 1):
                    return True

            board[row][col] = curr_char
            return False 


        for row in range(n):
            for col in range(m):
                if dfs(row, col, 0):
                    return True
        
        return False

   