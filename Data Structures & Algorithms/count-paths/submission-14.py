class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * (m)

        for i in range(n - 1):
            next_dp = [1] * m
            for j in range(m - 2, -1, -1):
                next_dp[j] = dp[j] + next_dp[j + 1]
            dp = next_dp
        return dp[0]