class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        memo = {}

        def dfs(i, j):
            if j == m:
                return 0 if i == n else n - i
            
            if i == n:
                return m - j

            if (i, j) in memo:
                return memo[(i, j)]

            res = float("inf")
            # if we have match
            if word1[i] == word2[j]:
                res = min(res, dfs(i + 1, j + 1))
            else:
                #insert
                res = min(res, 1 + dfs(i, j + 1))

                #delete
                res = min(res, 1 + dfs(i + 1, j))

                #replace
                res = min(res, 1 + dfs(i + 1, j + 1))

            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)