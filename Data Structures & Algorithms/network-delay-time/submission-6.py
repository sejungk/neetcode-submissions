class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((t, v))

        visited = set()
        min_heap = [(0, k)]
        curr_time = 0
        while min_heap:
            t, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            curr_time = t
            for nei_t, nei in adj[node]:
                heapq.heappush(min_heap, (nei_t + curr_time, nei))
            
        return curr_time if len(visited) == n else -1
