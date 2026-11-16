class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n + 2)
        prev1 = 0
        prev2 = 0

        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, dp[i]
        return min(dp[0], dp[1])