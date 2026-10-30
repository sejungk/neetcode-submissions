class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [None] * n

        def dfs(i):
            if i == n - 1:
                return 0
                
            if memo[i]:
                return memo[i]

            farthest = min(i + nums[i], n - 1)
            best = float("inf")

            for next_idx in range(i + 1, farthest + 1):
                best = min(best, 1 + dfs(next_idx))

            memo[i] = best
            return best

        return dfs(0)