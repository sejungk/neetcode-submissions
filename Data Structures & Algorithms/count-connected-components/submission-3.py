class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited = set()

        for i in range(n):
            adj[i] = []

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def bfs(node):
            queue = deque([node])

            while queue:
                node = queue.popleft()

                for nei in adj[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
        
        count = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1

        return count