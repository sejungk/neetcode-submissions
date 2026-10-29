class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        shortest = len(min(wordDict, key=len))
        for i in range(shortest, (n + 1)):
            for word in wordDict:
                if s[i-len(word): i] == word:
                    if dp[i - len(word)] == True or i - len(word) == 0:
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