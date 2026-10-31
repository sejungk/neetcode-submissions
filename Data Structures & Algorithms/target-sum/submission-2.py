class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, amount):
            if i == n:
                if amount == 0:
                    return 1
                else:
                    return 0
            
            if (i, amount) in memo:
                return memo[(i, amount)]

            memo[(i, amount)] = dfs(i + 1, amount - nums[i]) + dfs(i + 1, amount + nums[i])
            return memo[(i, amount)]

        return dfs(0, target)