class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, height, visited, cycle):

            if i in visited:
                return visited[i]

            if i in cycle:
                return 0
            
            cycle.add(i)

            max_height = height
            for j in adj[i]:
                max_height = max(max_height, dfs(j, height + 1, visited, cycle))

            cycle.remove(i)
            visited[i] = max_height
            return max_height

        min_height = float("inf")
        res = []
        for i in range(n):
            visited = {}
            cycle = set()
            height = dfs(i, 0, visited, cycle)
            print(height)
            if height < min_height:
                min_height = height
                res = [i]
            elif height == min_height:
                res.append(i)
        
        return res