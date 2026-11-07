class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        
        max_sum = -float("inf")
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
            max_sum = max(max_sum, dp[i])

        return max_sum

