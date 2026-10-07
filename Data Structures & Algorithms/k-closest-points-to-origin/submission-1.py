class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = math.sqrt((x * x) + (y * y))
            heapq.heappush(min_heap, [-dist, x, y])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        while min_heap:
            d, x, y = heapq.heappop(min_heap)
            res.append([x, y])
        
        return res