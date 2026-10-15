class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx = 0
        res_len = 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, - 1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    # update max length
                    curr_len = j - i + 1
                    if res_len < curr_len:
                        res_idx = i
                        res_len = j - i + 1
        
        return s[res_idx : res_idx + res_len]