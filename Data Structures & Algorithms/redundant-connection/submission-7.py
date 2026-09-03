class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_graph = {}
        for a, b in edges:
            adj_graph.setdefault(a, []).append(b)
            adj_graph.setdefault(b, []).append(a)
        
        n = len(edges)

        def dfs(node, prev, ignore_edge, visited):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj_graph[node]:
                if neighbor == prev:
                    continue
                if ((node == ignore_edge[0] and neighbor == ignore_edge[1]) or 
                (node == ignore_edge[1] and neighbor == ignore_edge[0])):
                    continue
                if dfs(neighbor, node, ignore_edge, visited) == False:
                    return False
                
            return True


        for a, b in reversed(edges):
            visited = set()
            if dfs(a, b, [a, b], visited) == True and len(visited) == n:
                return [a, b]
            