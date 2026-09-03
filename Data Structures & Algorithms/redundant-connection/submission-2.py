class Solution:
    def findRedundantConnection(self, ignore_edges: List[List[int]]) -> List[int]:
        adj_graph = {}
        vertices = set()
        for a, b in ignore_edges:
            adj_graph.setdefault(a, []).append(b)
            adj_graph.setdefault(b, []).append(a)
            vertices.add(a)
            vertices.add(b)
        
        n = len(vertices)

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


        for a, b in reversed(ignore_edges):
            visited = set()
            if dfs(a, b, [a, b], visited) == True and len(visited) == n:
                return [a, b]
            