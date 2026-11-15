class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_dist = [float("inf")] * n

        min_dist[0] = 0
        res = 0

        for _ in range(n):
            min_cost = float("inf")
            curr = -1

            for i in range(n):
                if i not in visited and min_dist[i] < min_cost:
                    min_cost = min_dist[i]
                    curr = i

            visited.add(curr)
            res += min_cost

            x1, y1 = points[curr]

            for i in range(n):
                if i not in visited:
                    x2, y2 = points[i]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[i] = min(min_dist[i], dist)

        return res