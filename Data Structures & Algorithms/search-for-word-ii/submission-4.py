class Node:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])

        def build_trie():
            root = Node()
                
            for word in words:
                curr = root
                for char in word:
                    if char not in curr.children:
                        curr.children[char] = Node()
                    
                    curr = curr.children[char]
                curr.word = word

            return root

        res = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(row, col, node):
            if node.word:
                res.add(node.word)

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < n and 0 <= nc < m:
                    temp = board[row][col]
                    board[row][col] = ""
                    neighbor_char = board[nr][nc]
                    if neighbor_char in node.children:
                        dfs(nr, nc, node.children[neighbor_char])
                    board[row][col] = temp

        root = build_trie()
        for row in range(n):
            for col in range(m):
                curr = root
                char = board[row][col]
                if char in curr.children:
                    dfs(row, col, curr.children[char])

        return list(res)
        

        