class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text2)
        m = len(text1)

        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if dp[i][j]:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = max(1 + dfs(i + 1, j + 1), dfs(i + 1, j + 1))
            else:
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        return dfs(0, 0)