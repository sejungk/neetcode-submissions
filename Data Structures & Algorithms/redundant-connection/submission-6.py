class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_graph = {}
        n = len(adj_graph) 

        def dfs(node, prev, visited):
            if node in visited:
                return True

            visited.add(node)
            for neighbor in adj_graph[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node, visited):
                    return True
            return False


        for a, b in edges:
            visited = set()
            adj_graph.setdefault(a, []).append(b)
            adj_graph.setdefault(b, []).append(a)
            if dfs(a, -1, visited):
                return [a, b]
        
        return []