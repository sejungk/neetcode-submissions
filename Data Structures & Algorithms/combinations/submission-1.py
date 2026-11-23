class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        used = [False] * (n + 1)

        def dfs(i, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            if i > n or used[i]:
                return
            
            dfs(i + 1, arr)

            arr.append(i)
            used[i] = True
            dfs(i + 1, arr)
            used[i] = False
            arr.pop()

        dfs(1, [])
        return res