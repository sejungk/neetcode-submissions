class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, height, parent):
            max_height = height

            for j in adj[i]:
                if j != parent:
                    max_height = max(max_height, dfs(j, height + 1, i))

            return max_height

        min_height = float("inf")
        res = []

        for i in range(n):
            height = dfs(i, 0, -1)

            if height < min_height:
                min_height = height
                res = [i]
            elif height == min_height:
                res.append(i)

        return res
