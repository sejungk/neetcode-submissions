class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, arr):
            if i == n:
                res.append(arr.copy())
                return

            arr.append(nums[i])
            dfs(i + 1, arr)
            arr.pop()

            dfs(i + 1, arr)

        dfs(0, [])
        return res