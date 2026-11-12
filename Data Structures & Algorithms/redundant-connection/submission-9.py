class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        n = len(edges)

        def dfs(node, visited):    
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei, visited)

        for a, b in reversed(edges):
            adj[a].remove(b)
            adj[b].remove(a)

            visited = set()
            dfs(1, visited)

            if len(visited) == n:
                return [a, b]

            adj[a].append(b)
            adj[b].append(a)
        return []