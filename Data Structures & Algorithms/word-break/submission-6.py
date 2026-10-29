class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        shortest = len(min(wordDict, key=len))
        for i in range(shortest, (n + 1)):
            for word in wordDict:
                start = i - len(word)
                if start >= 0 and dp[start] and s[start: i] == word:
                    dp[i] = True
        
        return dp[n]

        