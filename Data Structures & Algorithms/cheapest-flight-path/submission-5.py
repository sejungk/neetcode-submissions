class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        dist = [[float("inf")] * (k + 2) for _ in range(n)] # + 2 for src and dts
        for from_airport, to_airport, price in flights:
            adj[from_airport].append([to_airport, price])

        dist[src][0] = 0
        min_heap = [(0, src, 0)]
        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)
            if dst == node:
                return cost

            if stops == k + 1 or dist[node][stops] < cost:
                continue
            
            for neighbor, neighbor_cost in adj[node]:
                new_cost = cost + neighbor_cost
                next_stops = 1 + stops
                if dist[neighbor][next_stops] > new_cost:
                    dist[neighbor][next_stops] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor, next_stops))
        
        return -1