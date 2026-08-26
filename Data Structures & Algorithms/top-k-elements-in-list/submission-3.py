class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        max_heap = []

        for num in nums:
             count[num] = count.get(num, 0) + 1
        
        for key, num in count.items():
            heapq.heappush(max_heap, (num, key))
            # any time size of heap is k + 1 remove the smallest to keep the heap size at k
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])
        return result