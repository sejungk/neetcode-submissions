class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [0] * (n + 1) 
        
        for i in range(m - 1, -1, -1):
            next_dp = [0] * (n + 1) 
            for j in range(n - 1, -1, -1):
                if text2[i] == text1[j]:
                    next_dp[j] = 1 + dp[j + 1]
                else:
                    next_dp[j] = max(dp[j], next_dp[j + 1])
            dp = next_dp   
        return dp[0]
    
    # Time Complexity: O(n * m)
    # Space Complexity: O(n * m)

        # c a t ()
    # c   3 2  1 0
    # r   2 2  1 0
    # a   2 2  1 0
    # b   1 1  1 0
    # t   1 1  1 0
    # ()  0 0  0 0