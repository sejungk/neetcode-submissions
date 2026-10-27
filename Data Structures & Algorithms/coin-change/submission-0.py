class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for target in range(1, amount + 1):
            for coin in coins:
                if coin <= target:
                    dp[target] = min(dp[target], dp[target - coin] + 1)
                
        return dp[amount] if dp[amount] != float("inf") else -1
                