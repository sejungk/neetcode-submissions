class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if word1 == word2:
                continue

            min_len = min(len(word1), len(word2))
            j = 0
            while j < min_len and word1[j] == word2[j]:
                j += 1

            if j == len(word1):
                continue

            if word1[j] and j == len(word2):
                return False
            
            if word1[j] and word2[j]:
                if order.index(word1[j]) > order.index(word2[j]):
                    return False

        return True
