class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)} # i : [cost, node]

        # build adj list
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        min_heap = [[0, 0]]
        while len(visit) < len(points):
            cost, i = heapq.heappop(min_heap)
            
            if i in visit:
                continue

            res += cost
            visit.add(i)

            for j in adj[i]:
                if j[1] not in visit:
                    heapq.heappush(min_heap, j)


        return res