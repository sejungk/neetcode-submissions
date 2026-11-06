class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, arr, count):
            if i >= n or count > target:
                return 

            if count == target:
                res.append(arr.copy())
                return 

            dfs(i + 1, arr, count)

            arr.append(nums[i])
            dfs(i, arr, nums[i] + count)
            arr.pop()
            
        dfs(0, [], 0)
        return res