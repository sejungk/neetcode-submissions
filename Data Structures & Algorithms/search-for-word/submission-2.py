class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, curr_word, visited):
            nonlocal directions
            nonlocal n
            nonlocal m

            if row < 0 or row >= n or col < 0 or col >= m:
                return False

            if (row, col) in visited: 
                return False

            new_word = curr_word + board[row][col]
            
            if not word.startswith(new_word):
                return False

            if new_word == word:
                return True

            visited.add((row, col))
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if dfs(new_row, new_col, new_word, visited):
                    return True

            visited.remove((row, col))
            return False 


        for row in range(n):
            for col in range(m):
                if dfs(row, col, "", set()):
                    return True
        
        return False

   