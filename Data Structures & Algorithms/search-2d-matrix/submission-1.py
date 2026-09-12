class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = ROWS * COLS - 1

        def key_to_pos(num):
            row = num // COLS
            col = num % COLS
            return (row, col)

        while left <= right:
            mid = (left + right) // 2
            row, col = key_to_pos(mid)

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                right -= 1
            
            else:
                left += 1

        return False