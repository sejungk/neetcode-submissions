class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, arr, total_sum):
            if total_sum == target:
                res.append(arr.copy())
                return

            if i >= len(candidates) or total_sum > target:
                return
            
            arr.append(candidates[i])
            dfs(i + 1, arr, total_sum + candidates[i])
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            skip = dfs(i + 1, arr, total_sum)

        dfs(0, [], 0)
        return res