class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(i, subset, total):
            if total > target or i >= len(nums):
                return 
            
            if total == target:
                res.append(subset)
                return

            dfs(i, subset + [nums[i]], total + nums[i])
            dfs(i + 1, subset, total)
        
        dfs(0, [], 0)
        return res