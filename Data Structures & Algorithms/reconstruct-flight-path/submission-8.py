class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for a, b in tickets:
            adj[a].append(b)
        
        res = []
        def dfs(node):    
            while adj[node]:
                neighbor = adj[node].pop()
                dfs(neighbor)
            res.insert(0, node)

        dfs("JFK")
        return res