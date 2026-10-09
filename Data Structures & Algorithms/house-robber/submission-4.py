class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        n = len(dp)
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i-1])
            
        return dp[-1] 

# [2, 9, 8, 3, 6]
# [2, 9, 10, 12, 16]