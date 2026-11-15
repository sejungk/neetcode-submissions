class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seen = defaultdict(int)
        for task in tasks:
            seen[task] += 1

        max_heap = []
        for task in seen:
            heapq.heappush(max_heap, (-seen[task], task))

        time = 0
        cooldown = []
        while max_heap or cooldown:
            if max_heap:
                count, task = heapq.heappop(max_heap)
                new_count = count + 1
                
                if new_count < 0:
                    heapq.heappush(cooldown, (time, task, new_count))
           
            time += 1
            while cooldown and cooldown[0][0] < (time - n):
                prev_time, task, count = heapq.heappop(cooldown)
                heapq.heappush(max_heap, (count, task))
            
        return time 