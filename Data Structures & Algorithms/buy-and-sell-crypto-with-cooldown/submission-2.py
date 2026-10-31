class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 2)]
        
        def dfs(i, holding):
            if i >= n:
                return 0

            if dp[i][holding]:
                return dp[i][holding]

            if holding:
                dp[i][holding] = max(prices[i] + dfs(i + 2, 0), dfs(i + 1, holding))
            if not holding:
                dp[i][holding] = max(-prices[i] + dfs(i + 1, 1), dfs(i + 1, holding))
            
            return dp[i][holding]

        return dfs(0, 0)