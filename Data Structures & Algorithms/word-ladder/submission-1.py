class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        variations = {}

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                variations.setdefault(key, []).append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist

            if word in visited:
                continue

            visited.add(word)
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                if not key in variations:
                    continue
                
                for neighbor in variations[key]:
                    queue.append((neighbor, dist + 1))

        return 0