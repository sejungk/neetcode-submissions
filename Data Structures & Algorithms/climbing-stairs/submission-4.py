class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def dfs(step):
            if step >= n:
                return step == n
            
            if dp[step] != -1:
                return dp[step]

            dp[step] = dfs(step + 1) + dfs(step + 2)
            return dp[step]
            
        return dfs(0)