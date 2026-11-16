class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums) / 2

        # [1,2,3,4,5] t = 7.5
        # 0, 0 
        # dfs(1, 1)
        # dfs(2, 3)
        # 

        memo = {}
        def dfs(i, curr_sum):
            if curr_sum == target:
                return True

            if i == n:
                return False

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            take = dfs(i + 1, curr_sum + nums[i])
            skip = dfs(i + 1, curr_sum)

            if take or skip:
                memo[(i, curr_sum)] = True
                return True
            
            memo[(i, curr_sum)] = False
            return False

        return dfs(0, 0)