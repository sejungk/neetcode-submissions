class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            if i > n:
                return
            
            dfs(i + 1, arr)

            arr.append(i)
            dfs(i + 1, arr)
            arr.pop()

        dfs(1, [])
        return res