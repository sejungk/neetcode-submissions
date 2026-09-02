class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_graph = {}
        potential_roots = set()

        for i in range(n):
            adj_graph[i] = []

        for a, b in edges:
            adj_graph[a].append(b)
            adj_graph[b].append(a)
        
        cycle = set()
        visited = set()
        def dfs(node, prev):
            if node == prev:
                return True
                
            if node in cycle and node != prev:
                return False

            if node in visited:
                return True
            
            cycle.add(node)
            for neighbor in adj_graph[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node) == False:
                    return False
            cycle.remove(node)
            visited.add(node) 

        if dfs(0, -1) == False:
            return False

        return len(visited) == n