class Solution:
    def foreignDictionary(self, words: List[str]) -> str:        
        adj = {char: set() for word in words for char in word}
        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]

            if prev.startswith(curr) and len(prev) > len(curr):
                return ""

            for j in range(min(len(prev), len(curr))):
                if prev[j] != curr[j]:
                    adj[prev[j]].add(curr[j])
                    break
                
        visited = set()
        visiting = set()
        res = []
        def cycle(node):
            if node in visited:
                return False
            
            if node in visiting:
                return True
            
            visiting.add(node)
            for nei in adj[node]:
                if cycle(nei):
                    return True

            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return False

        for node in adj:
            if cycle(node):
                return ""
        
        return "".join(reversed(res))
            
