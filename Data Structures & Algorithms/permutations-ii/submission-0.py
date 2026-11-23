class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        used = [False] * n

        def dfs(arr):
            if len(arr) == n:
                res.append(arr.copy())
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                arr.append(num)
                used[i] = True
                dfs(arr)
                used[i] = False
                arr.pop()

        dfs([])
        return res