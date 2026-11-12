class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        adj = defaultdict(list)

        for i in range(len(beginWord)):
            key = beginWord[:i] + "*" + beginWord[i + 1:]
            adj[key] = [beginWord]

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                adj[key].append(word)

        visited = set()
        visited.add(beginWord)
        queue = deque([(beginWord, 1)])
        while queue:
            word, dist = queue.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:] 
                for nei in adj[key]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))
        return 0