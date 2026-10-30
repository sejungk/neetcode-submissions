class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                continue

            for k in range(i, i + nums[i] + 1):
                if dp[k] == True:
                    dp[i] = True
                    break

        return dp[0]