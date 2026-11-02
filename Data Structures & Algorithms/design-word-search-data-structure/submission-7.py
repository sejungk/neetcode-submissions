class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            curr = node

            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if (dfs(child, i + 1)):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end
        return dfs(self.root, 0)