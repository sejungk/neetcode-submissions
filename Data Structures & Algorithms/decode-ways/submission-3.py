class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        memo = {}
        def dfs(i):
            if i >= n:
                return 1

            if i in memo:
                return memo[i]

            count = 0
            if i + 1 < n and "10" <= s[i:i + 2] <= "26":
                count += dfs(i + 2)
            
            if s[i] > "0":
                count += dfs(i + 1)

            memo[i] = count
            return count

        return dfs(0)