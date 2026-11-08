class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}
        def dfs(i, prev):
            if i == n:
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            res = -float("inf")
            if prev < nums[i]:
                res = 1 + dfs(i + 1, nums[i])
            
            res = max(res, dfs(i + 1, prev))
            memo[(i, prev)] = res
            return res

        return dfs(0, -float("inf"))