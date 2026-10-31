class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(n + 1)]

        def dfs(i, curr_amt):
            if curr_amt == 0:
                return 1
            
            if i >= n:
                return 0

            if memo[i][curr_amt] != -1:
                return memo[i][curr_amt]

            res = 0
            if curr_amt >= coins[i]:
                res += dfs(i + 1, curr_amt) + dfs(i, curr_amt - coins[i])
            
            memo[i][curr_amt] = res
            return res

        return dfs(0, amount)
                