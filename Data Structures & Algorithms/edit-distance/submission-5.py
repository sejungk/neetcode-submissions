class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [0] * (n + 1)
        for j in range(n + 1):
            dp[j] = n - j

        for i in range(m - 1, -1 , -1):
            next_dp = dp[n] # saving [i + 1][j + 1] spot
            dp[n] = m - i

            for j in range(n - 1, -1, -1):
                temp = dp[j] #save [i + 1][j] spot
                if word1[i] == word2[j]:
                    dp[j] = next_dp
                else:
                    dp[j] = 1 + min(dp[j + 1], temp, next_dp)

                next_dp = temp

        return dp[0]

        