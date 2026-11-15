class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = 0
        dist = [float("inf")] * n
        visit = set()
        edges = 0
        res = 0

        while edges < n - 1:
            visit.add(node)
            next_node = -1
            for i in range(n):
                if i in visit:
                    continue

                curr_dist = (abs(points[i][0] - points[node][0]) + 
                            abs(points[i][1] - points[node][1]))
                            
                dist[i] = min(dist[i], curr_dist)
                if next_node == -1 or dist[i] < dist[next_node]:
                    next_node = i
            
            res += dist[next_node]
            node = next_node
            edges += 1
        return res