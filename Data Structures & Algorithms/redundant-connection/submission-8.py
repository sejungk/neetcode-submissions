class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, prev):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                
                if dfs(neighbor, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
                
        dfs(1, -1)

        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]
        
        return []