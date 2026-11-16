class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n + 2)
        dp[n] = 0
        dp[n + 1] = 0
        # dp[n-1] = cost[n-1]

        # [I, I, I, 0]
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 2], dp[i + 1])
        return min(dp[0], dp[1])