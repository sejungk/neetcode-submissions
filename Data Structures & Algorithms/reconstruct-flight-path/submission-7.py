class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            src = stack[-1]
            if not adj[src]:
                res.append(stack.pop())
            else:
                stack.append(adj[src].pop())
            
        return res[::-1]