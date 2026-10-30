class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[None] * (n ) for _ in range(n )]

        def dfs(i, open):
            if open < 0:
                return False
            if i == n:
                return open == 0

            if memo[i][open] is not None:
                return memo[i][open]
                
            if s[i] == "(":
                memo[i][open] = dfs(i + 1, open + 1)
            elif s[i] == ")":
                memo[i][open] = dfs(i + 1, open - 1)
            else:
                memo[i][open] = (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))

            return memo[i][open]

        return dfs(0, 0)