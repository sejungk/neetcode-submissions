class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        prev = self.root

        for char in prefix:
            if char not in prev.children:
                return False
            
            prev = prev.children[char]
        
        return True
        
        