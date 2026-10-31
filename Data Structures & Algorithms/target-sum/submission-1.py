class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, amt):
            if i == n:
                if amt == 0:
                    return 1
                else:
                    return 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]

            memo[(i, amt)] = dfs(i + 1, amt - nums[i]) + dfs(i + 1, amt + nums[i])
            return memo[(i, amt)]

        return dfs(0, target)