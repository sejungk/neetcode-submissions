class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def dfs(i, amt):
            if amt == amount:
                return 0

            if i == n or amt > amount:
                return float("inf")

            if (i, amt) in memo:
                return memo[(i, amt)]

            res = float("inf")
            if amt + coins[i] <= amount:
                res = min(res, 1 + dfs(i, amt + coins[i]))

            res = min(res, dfs(i + 1, amt))

            memo[(i, amt)] = res
            return memo[(i, amt)]
            
        res = dfs(0, 0)
        if res == float("inf"):
            return -1
        else:
            return res