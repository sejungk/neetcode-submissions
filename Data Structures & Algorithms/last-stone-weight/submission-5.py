class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        final = 0
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            
            if stone1 == stone2:
                final = 0
            else:
                final = abs(stone1 - stone2)
                heapq.heappush(max_heap, -final)
        
        if max_heap:
            return max_heap[0] * -1
        else:
            return final
