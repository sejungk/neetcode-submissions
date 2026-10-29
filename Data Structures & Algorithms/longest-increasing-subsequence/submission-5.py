class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, prev_index):
            if i == n:
                return 0

            # Shift by 1 so prev_index == -1 ("no previous element") maps to column 0.
            if memo[i][prev_index + 1] != -1:
                return memo[i][prev_index + 1]

            # Skip nums[i]
            best = dfs(i + 1, prev_index)

            # Take nums[i]
            if prev_index == -1 or nums[prev_index] < nums[i]:
                best = max(best, 1 + dfs(i + 1, i))

            memo[i][prev_index + 1] = best
            return best

        return dfs(0, -1)