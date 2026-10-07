class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = math.sqrt((x * x) + (y * y))
            heapq.heappush(min_heap, [dist, x, y])
        
        res = []
        while k:
            dist, x, y, = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1
        
        return res