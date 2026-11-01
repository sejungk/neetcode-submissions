class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dfs(nums):
            if len(nums) == 2:
                return 0

            if (tuple(nums)) in memo:
                return memo[(tuple(nums))]

            max_coins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(nums[:i] + nums[i + 1:])
                max_coins = max(max_coins, coins)
            
            memo[(tuple(nums))] = max_coins
            return max_coins

        return dfs(nums)