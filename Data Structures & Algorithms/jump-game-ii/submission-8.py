class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}
        def dfs(i):
            if i == n - 1:
                return 0
            
            if i >= n:
                return float("inf")
            
            if i in memo:
                return memo[i]

            min_jumps = float("inf")
            for j in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + dfs(i + j))
            memo[i] = min_jumps
            return min_jumps
        return dfs(0)