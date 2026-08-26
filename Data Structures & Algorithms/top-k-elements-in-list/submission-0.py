class Solution:
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       frequency = defaultdict(int)

       for num in nums:
           frequency[num] += 1
       
       max_heap = []
       for key in frequency:
           heapq.heappush(max_heap, (-frequency[key], key))

       result = []
       for i in range(k):
           freq, num = heapq.heappop(max_heap)
           result.append(num)

       return result