class Node:

    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word):
                return node.end == True

            if word[i] != "." and word[i] not in node.children:
                return False

            if word[i] == ".":
                for val in node.children:
                    if dfs(node.children[val], i + 1):
                        return True
                return False
            
            return dfs(node.children[word[i]], i + 1)

        return dfs(self.root, 0)
            

