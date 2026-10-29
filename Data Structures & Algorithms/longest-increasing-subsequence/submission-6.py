class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]
        
        def dfs(i, j):
            if i == n:
                return 0

            # if seen, return saved val
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            # skip
            max_count = dfs(i + 1, j)

            #take if we have no prev, or j is less than i
            if j == -1 or nums[j] < nums[i]:
                max_count = max(max_count, 1 + dfs(i + 1, i))

            memo[i][j + 1] = max_count
            return max_count

        return dfs(0, -1)
        