class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}

        for i in range(n):
            adj[i] = []

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def cycle(node, prev):
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei != prev:
                    if cycle(nei, node):
                        return True
            
            return False
            
        if cycle(0, -1):
            return False 

        return len(visited) == n
            

        