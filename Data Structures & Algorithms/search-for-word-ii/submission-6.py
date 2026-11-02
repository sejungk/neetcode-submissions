class Node:
    def __init__(self):
        self.children = {}
        self.word = ""

    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS = len(board)
        COLS = len(board[0])
        root = Node()

        for word in words:
            root.add_word(word)

        res = set()
        def dfs(row, col, node):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or 
                board[row][col] not in node.children
            ):
                return 

            node = node.children[board[row][col]]
            
            if node.word:
                res.add(node.word)

            for dr, dc in directions:
                temp = board[row][col]
                board[row][col] = ""
                dfs(row + dr, col + dc, node)
                board[row][col] = temp

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root)

        return list(res)
        