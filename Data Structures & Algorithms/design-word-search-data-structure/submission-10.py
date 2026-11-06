class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(i, curr):
            if i == n:
                return curr.end
            
            char = word[i]
            if char == ".":
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if char not in curr.children:
                    return False
            return dfs(i + 1, curr.children[char])

        return dfs(0, self.root)
        
