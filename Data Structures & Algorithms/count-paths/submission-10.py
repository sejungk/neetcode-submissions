class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n-1] = 1

        for row in range(m):
            for col in range(n - 1, -1, -1):
                dp[col] += dp[col + 1]

        return dp[0]