class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = math.sqrt((x * x) + (y * y))
            heapq.heappush(max_heap, (-dist, [x, y]))
        
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        while max_heap:
            dist, coord = heapq.heappop(max_heap)
            res.append(coord)
        return res