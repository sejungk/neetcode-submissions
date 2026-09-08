class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        variations = {}

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                variations.setdefault(key, []).append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist

            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                if not key in variations:
                    continue
                
                for neighbor in variations[key]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))
                        visited.add(neighbor)

        return 0