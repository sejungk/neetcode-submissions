class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-count for count in count.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown_tasks = deque()
        while max_heap or cooldown_tasks:
            time += 1

            if not max_heap:
                time = cooldown_tasks[0][1]
            else:
                count = 1 + heapq.heappop(max_heap)
                if count < 0:
                    cooldown_tasks.append([count, time + n])
            if cooldown_tasks and cooldown_tasks[0][1] == time:
                heapq.heappush(max_heap, cooldown_tasks.popleft()[0])
        return time