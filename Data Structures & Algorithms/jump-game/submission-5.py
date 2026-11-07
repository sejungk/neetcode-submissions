class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[n-1] = True

        for i in range(n-1, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if dp[j] == True:
                    dp[i] = True
                    break
        
        
        return dp[0]