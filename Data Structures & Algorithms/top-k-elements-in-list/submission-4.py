class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        min_heap = []

        for num in nums:
            count[num] += 1
        
        for key in count:
            heapq.heappush(min_heap, (count[key], key))

            while len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        while min_heap:
            c, k = heapq.heappop(min_heap)
            res.append(k)

        return res
