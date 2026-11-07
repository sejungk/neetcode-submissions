class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        memo = {}
        def dfs(i, end):
            if i >= end:
                return 0

            if (i, end) in memo:
                return memo[(i, end)]
 
            memo[(i, end)] = max(dfs(i + 1, end), nums[i] + dfs(i + 2, end))
            return memo[(i, end)]

        return max(dfs(1, n), dfs(0, n - 1))