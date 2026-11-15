class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        min_heap = [(0, 0)] # dist, node idx
        visited = set()
        res = 0

        while len(visited) < len(points):
            dist, node = heapq.heappop(min_heap)
            x1, y1 = points[node]

            if node in visited:
                continue
                
            visited.add(node)
            res += dist

            for i in range(len(points)):
                if i not in visited:
                    x2, y2 = points[i]
                    curr_dist = abs(x1 - x2) + abs(y1 - y2)

                    heapq.heappush(min_heap, (curr_dist, i))

        return res

