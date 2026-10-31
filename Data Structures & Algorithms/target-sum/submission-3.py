class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]
        



        # for i in range(n)

        # def dfs(i, amount):
        #     if i == n:
        #         if amount == 0:
        #             return 1
        #         else:
        #             return 0
            
        #     if (i, amount) in memo:
        #         return memo[(i, amount)]

        #     memo[(i, amount)] = dfs(i + 1, amount - nums[i]) + dfs(i + 1, amount + nums[i])
        #     return memo[(i, amount)]

        # return dfs(0, target)