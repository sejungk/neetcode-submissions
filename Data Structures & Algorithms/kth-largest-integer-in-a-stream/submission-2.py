class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.max_heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        
        removed = []
        for i in range(self.k - 1):
            removed.append(heapq.heappop(self.max_heap))
        
        kth_int = heapq.heappop(self.max_heap) 
        removed.append(kth_int)

        while removed:
            heapq.heappush(self.max_heap, removed.pop())

        return kth_int * -1