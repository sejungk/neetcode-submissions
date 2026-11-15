class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seen = defaultdict(int)
        
        for task in tasks:
            seen[task] += 1

        max_heap = []
        for task in seen:
            heapq.heappush(max_heap, (-seen[task], task))

        max_freq, task = heapq.heappop(max_heap)
        sections = -max_freq - 1
        open_tasks = (sections) * n

        while max_heap:
            count, task = heapq.heappop(max_heap)
            open_tasks -= min(-count, sections)

        return len(tasks) + max(0, open_tasks)