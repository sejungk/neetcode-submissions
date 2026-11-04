class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n - 1] = 1

        for row in range(m - 1, - 1, -1):
            next_dp = [0] * (n + 1)
            for col in range(n - 1, -1, -1):
                next_dp[col] += next_dp[col + 1] + dp[col]
            dp = next_dp

        return dp[0]