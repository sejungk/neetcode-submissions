class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(i, curr_amt):
            if curr_amt == amount:
                return 1

            if i >= n or curr_amt > amount:
                return 0

            if (i, curr_amt) in memo:
                return memo[(i, curr_amt)]

            skip = dfs(i + 1, curr_amt)
            take = dfs(i, curr_amt + coins[i])

            memo[(i, curr_amt)] = skip + take
            return skip + take
            
        return dfs(0, 0)