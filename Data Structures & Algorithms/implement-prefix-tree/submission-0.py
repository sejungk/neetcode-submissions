class PrefixTree:

    def __init__(self):
        self.dictionary = {}   

    def insert(self, word: str) -> None:
        parent = self.dictionary
        for char in word:
            if char not in parent:
                parent[char] = {}
            
            parent = parent[char]

        parent["end"] = True
 
    def search(self, word: str) -> bool:
        parent = self.dictionary
        for char in word:
            if char not in parent:
                return False

            parent = parent[char]   
        return parent.get("end", False)

    def startsWith(self, prefix: str) -> bool:
        parent = self.dictionary
        for char in prefix:
            if char not in parent:
                return False
            
            parent = parent[char]
        return True
        
        