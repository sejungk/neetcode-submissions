class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        for a, b in tickets:
            adj[a].append(b)

        res = []
        def dfs(airport):
            while adj[airport]:
                nei = adj[airport].pop()
                dfs(nei)
            
            res.append(airport)
            return res

        dfs("JFK")
        return res[::-1]