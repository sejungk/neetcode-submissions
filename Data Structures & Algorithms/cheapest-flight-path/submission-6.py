class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for from_airport, to_airport, price in flights:
            adj[from_airport] = adj.get(from_airport, [])
            adj[from_airport].append([price, to_airport])
        
        visited = set()
        min_heap = [(0, src, 0)]
        while min_heap:
            cost, airport, steps = heapq.heappop(min_heap)

            if steps > k + 1 or (airport, steps) in visited:
                continue

            visited.add((airport, steps))
            
            if airport == dst:
                return cost
                
            for neighbor_price, neighbor_airport in adj.get(airport, []):
                if (neighbor_airport, steps + 1) not in visited:
                    heapq.heappush(min_heap, [cost + neighbor_price, neighbor_airport, steps + 1])
        return -1