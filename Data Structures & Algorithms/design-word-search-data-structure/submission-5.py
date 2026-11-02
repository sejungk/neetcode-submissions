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
        memo = {}

        def dfs(node, i):
            if i == len(word):
                return node.end

            if (node, i) in memo:
                return memo[(node, i)]

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        memo[(node, i)] = True
                        return True
                memo[(node, i)] = False
                return False
            
            if word[i] not in node.children:
                memo[(node, i)] = False
                return False

            memo[(node, i)] = dfs(node.children[word[i]], i + 1)
            return memo[(node, i)]

        return dfs(self.root, 0)
            

