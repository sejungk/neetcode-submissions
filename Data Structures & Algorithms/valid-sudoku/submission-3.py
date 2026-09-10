class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n =  len(board)
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                bit = 1 << val

                if (1 << bit) & rows[r]:
                    return False
                if (1 << bit) & cols[c]:
                    return False
                if (1 << bit) & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= (1 << bit)
                cols[c] |= (1 << bit)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << bit)
        return True
