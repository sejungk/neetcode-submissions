class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        word_length = len(wordList[0])
        word_set = set(wordList)
        queue_start, queue_end = deque([beginWord]), deque([endWord])
        from_start, from_end = {beginWord: 1}, {endWord: 1}

        while queue_start and queue_end:
            # if start queue is longer swap w end so its shorter
            if len(queue_start) > len(queue_end):
                queue_start, queue_end = queue_end, queue_start
                from_start, from_end = from_end, from_start

            for _ in range(len(queue_start)):
                word = queue_start.popleft()
                steps = from_start[word]

                for i in range(word_length):
                    for c in range(97, 123):
                        # if current char at is same at word[i] then skip
                        if chr(c) == word[i]:
                            continue
                        
                        # construct all valid neighbor variants of this current word swapping out just one char
                        neighbor = word[:i] + chr(c) + word[i+1:]

                        if neighbor not in word_set:
                            continue

                        if neighbor in from_end:
                            return steps + from_end[neighbor]
                        
                        if neighbor not in from_start:
                            from_start[neighbor] = steps + 1
                            queue_start.append(neighbor)
        
        return 0