class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        seen = defaultdict(set)

        def valid_row(row, col, digit):
            row_key = "row" + str(row)
            if digit in seen[row_key]:
                return False
            
            seen[row_key].add(digit)
            return True

        def valid_col(row, col, digit):
            col_key = "col" + str(col)
            if digit in seen[col_key]:
                return False
            
            seen[col_key].add(digit)
            return True

        def valid_box(row, col, digit):
            box_key = "box" + str((row // 3) * 3 + (col // 3))
            if digit in seen[box_key]:
                return False
            
            seen[box_key].add(digit)
            return True

        for row in range(n):
            for col in range(m):
                digit = board[row][col]
                
                if digit == ".":
                    continue

                if not valid_row(row, col, digit) or not valid_col(row, col, digit) or not valid_box(row, col, digit):
                    return False

        return True