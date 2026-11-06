class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                board[r][c] not in node.children
            ):
                return 


            node = node.children[board[r][c]]
            word.append(board[r][c]) 
            if node.isWord:
                res.add("".join(word.copy()))

            char = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                dfs(dr + r, c + dc, node, word)
            
            board[r][c] = char
            word.pop()

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, [])
        
        return list(res)