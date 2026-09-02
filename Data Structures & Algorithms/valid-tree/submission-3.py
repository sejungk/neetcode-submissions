class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_graph = {}

        for i in range(n):
            adj_graph[i] = []

        for a, b in edges:
            adj_graph[a].append(b)
            adj_graph[b].append(a)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node) 
            for neighbor in adj_graph[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node) == False:
                    return False
            

        if dfs(0, -1) == False:
            return False

        return len(visited) == n