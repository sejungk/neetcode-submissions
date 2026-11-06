class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def dfs(i, arr, count):
            if count == target:
                res.append(arr.copy())
                return 

            for j in range(i, n):
                if count + nums[j] > target:
                    return 

                arr.append(nums[j])
                dfs(j, arr, count + nums[j])
                arr.pop()

        dfs(0, [], 0)
        return res