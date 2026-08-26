class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        max_heap = []

        for num in nums:
             count[num] = count.get(num, 0) + 1
        
        for key, num in count.items():
            heapq.heappush(max_heap, (-num, key))

        result = []
        while k > 0:
            freq, num = heapq.heappop(max_heap)
            result.append(num)
            k -= 1

        return result