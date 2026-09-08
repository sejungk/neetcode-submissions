class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        def dfs(step):
            if step == n:
                return 1
            
            if step > n:
                return 0
            
            if dp[step]:
                return dp[step]

            dp[step] = dfs(step + 1) + dfs(step + 2)
            return dp[step]
        return dfs(0)