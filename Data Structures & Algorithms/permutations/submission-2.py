class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def dfs(arr):
            if len(arr) == n:
                res.append(arr.copy())
                return

            for i in range(n):
                if used[i]:
                    continue

                arr.append(nums[i])
                used[i] = True

                dfs(arr)

                arr.pop()
                used[i] = False

        dfs([])
        return res