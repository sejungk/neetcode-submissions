class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        m = len(wordList[0])
        adj = {word: [] for word in wordList}

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                cnt = 0

                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        cnt += 1

                if cnt == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])

        q = deque()
        res = 1
        visit = set()

        for i in range(m):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue

                word = beginWord[:i] + chr(c) + beginWord[i + 1:]

                if word in adj and word not in visit:
                    q.append(word)
                    visit.add(word)

        while q:
            res += 1

            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for neighbor in adj[word]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        q.append(neighbor)

        return 0