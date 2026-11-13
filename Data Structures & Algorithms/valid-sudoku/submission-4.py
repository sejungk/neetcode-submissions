class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        M = len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(N):
            for col in range(M):
                if board[row][col] != ".":
                    num = board[row][col]
                    square = (row // 3, col // 3)
                    if num in rows[row] or num in cols[col] or num in squares[square]:
                        return False
                    
                    rows[row].add(num)
                    cols[col].add(num)
                    squares[square].add(num)

        return True