class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        res = []
        visiting = set()
        visited = set()
        def check_cycle(node):
            if node in visiting:
                return True
            
            if node in visited:
                return False

            visiting.add(node)
            if node in adj:
                for neighbor in adj[node]:
                    if check_cycle(neighbor):
                        return True
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return False

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            min_len = min(len(first), len(second))

            if first[:min_len] == second[:min_len]:
                if len(first) > len(second):
                    return ""
                
            for j in range(min_len):
                if first[j] != second[j]:
                    adj[first[j]].add(second[j])
                    break
        
        for node in adj:
            if check_cycle(node):
                return ""
        
        return "".join(reversed(res))
