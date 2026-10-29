class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        shortest = len(min(wordDict, key=len))
        for i in range(shortest, (n + 1)):
            for word in wordDict:
                start = i - len(word)
                if (dp[start] or start == 0) and s[start: i] == word:
                    dp[i] = True
        
        return dp[n]

        
        # def dfs(start):
        #     if start >= n:
        #         return True

        #     for word in wordDict:
        #         end = start + len(word)
        #         if s[start : end] == word:
        #             if dfs(end):
        #                 return True

        #     return False

        # return dfs(0)