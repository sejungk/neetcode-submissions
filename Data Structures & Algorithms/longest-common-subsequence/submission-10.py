class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
    
        # c a t ()
    # c   3 2  1 0
    # r   2 2  1 0
    # a   2 2  1 0
    # b   1 1  1 0
    # t   1 1  1 0
    # ()  0 0  0 0