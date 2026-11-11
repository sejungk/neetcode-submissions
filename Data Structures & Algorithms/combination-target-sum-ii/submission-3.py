class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(i, arr, amt):
            if amt == target:
                res.append(arr.copy())
                return

            if amt > target or i == n:
                return

            arr.append(candidates[i])
            dfs(i + 1, arr, amt + candidates[i])
            arr.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, arr, amt)

        dfs(0, [], 0)
        return res
