class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        solution = []

        cols = set()
        diagonals = set()      
        anti_diagonals = set() 

        def backtrack(row):
            if row == n:
                res.append(solution.copy())

            for col in range(n):
                diag = row - col
                anti_diag = row + col

                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue
                
                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)
                solution.append("." * col + "Q" + "." * (n - col - 1))
                backtrack(row + 1)

                solution.pop()
                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)

        backtrack(0)
        return res