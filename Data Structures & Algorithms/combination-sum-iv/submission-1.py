class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        memo = {}
        def dfs(curr):            
            if curr == target:
                return 1
            
            if curr > target:
                return 0 

            if curr in memo:
                return memo[curr]

            count = 0
            for j in range(n):
                count += dfs(curr + nums[j])

            memo[curr] = count
            return count

        return dfs(0)