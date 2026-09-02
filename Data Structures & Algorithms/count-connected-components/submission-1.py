class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_graph = {}
        visited = set()
        count = 0

        for i in range(n):
            adj_graph[i] = []

        for a, b in edges:
            adj_graph[a].append(b)
            adj_graph[b].append(a)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbor in adj_graph[node]:
                dfs(neighbor)


        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            count += 1
        
        return count
