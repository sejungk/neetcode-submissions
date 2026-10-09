class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)} # i: list of [cost, node]
        
        # build adj list weighted dist and connected node
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        #prims
        res = 0
        visit = set()
        min_heap = [[0, 0]] #[cost, point]
        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            
            res += cost
            visit.add(i)

            for neighbor_cost, neighbor in adj[i]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, [neighbor_cost, neighbor])
        
        return res


