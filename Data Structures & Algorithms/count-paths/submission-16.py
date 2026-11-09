class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * (m)

        for i in range(n - 1):
            prev = 1
            for j in range(m - 2, -1, -1):
                dp[j] += prev
                prev = dp[j]
        return dp[0]