class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        memo = {}
        def dfs(i):
            if i == n:
                return 0
            
            if i > n:
                return float("inf")

            if i in memo:
                return memo[i]

            memo[i] = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))