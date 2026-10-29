class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, prev_index):
            if i == n:
                return 0

            memo_col = prev_index + 1
            if memo[i][memo_col] != -1:
                return memo[i][memo_col]

            # skip nums[i]
            best = dfs(i + 1, prev_index)  

            # take nums[i]
            if prev_index == -1 or nums[prev_index] < nums[i]:
                best = max(best, 1 + dfs(i + 1, i))  

            memo[i][memo_col] = best
            return best

        return dfs(0, -1)