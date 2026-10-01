class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, arr, total_sum):
            if total_sum == target:
                res.append(arr)
                return

            if i >= len(candidates) or total_sum > target:
                return
            
            take = dfs(i + 1, arr + [candidates[i]], total_sum + candidates[i])
            skip_idx = i
            while skip_idx < len(candidates) - 1 and candidates[skip_idx] == candidates[skip_idx + 1]:
                skip_idx += 1
            skip = dfs(skip_idx + 1, arr, total_sum)

        dfs(0, [], 0)
        return res