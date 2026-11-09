class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (m + 1)
        dp[m - 1] = 1

        for i in range(n - 1, -1 ,-1):
            next_dp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                next_dp[j] += dp[j] + next_dp[j + 1]
            dp = next_dp
        return dp[0]