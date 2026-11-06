class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class Solution:

    def add_words(self, words):
        root = TrieNode()

        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.end = True
        return root

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        root = self.add_words(words)
        res = []

        def dfs(row, col, curr, word):
            if curr.end:
                curr.end = False
                res.append("".join(word.copy()))

            char = board[row][col]
            board[row][col] = "#"  # mark this cell used 

            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col
                if 0 <= new_row < ROWS and 0 <= new_col and new_col < COLS:
                    next_char = board[new_row][new_col]
                    if next_char in curr.children:
                        word.append(next_char)
                        dfs(new_row, new_col, curr.children[next_char], word)
                        word.pop()
            board[row][col] = char

        for row in range(ROWS):
            for col in range(COLS):
                char = board[row][col]
                if char in root.children:
                    dfs(row, col, root.children[char], [char])

        return list(res)
        