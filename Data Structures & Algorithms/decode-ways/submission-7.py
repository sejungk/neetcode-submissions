class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i < n - 1 and "10" <= s[i: i + 2] <= "26":
                dp[i] += dp[i + 2]

        return dp[0]
