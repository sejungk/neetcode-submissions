class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            new_stone = -heapq.heappop(stones) + heapq.heappop(stones)
            if new_stone > 0:
                heapq.heappush(stones, -new_stone)
            
        return -stones[0] if stones else 0
