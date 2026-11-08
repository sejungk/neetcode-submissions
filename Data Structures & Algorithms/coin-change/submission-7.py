class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        memo = {}
        def dfs(count):
            if count == amount:
                return 0

            if count > amount:
                return float("inf")

            if count in memo:
                return memo[count]

            res = float("inf")
            for i in range(n):
                res = min(res, 1 + dfs(count + coins[i]))
            
            memo[count] = res
            return res

        res = dfs(0)
        return res if res != float("inf") else -1