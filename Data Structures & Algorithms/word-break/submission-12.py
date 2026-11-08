class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                w = len(word)
                if i + w <= n and s[i: i + w] == word:
                    if dp[i + w]:
                        dp[i] = dp[i + w]
                        break
        print(dp)
        return dp[0]
                    
