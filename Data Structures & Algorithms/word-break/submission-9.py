class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        memo = {}
        def dfs(i):
            if i == n:
                return True
            
            if i in memo:
                return memo[i]

            for word in wordDict:
                word_len = len(word)
                if s[i: i + word_len] == word:
                    if dfs(i + word_len):
                        return True
            memo[i] = False
            return False

        return dfs(0)