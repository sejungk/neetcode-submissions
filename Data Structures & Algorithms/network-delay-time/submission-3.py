class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        total_time = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            total_time = time

            for neighbor, neighbor_time in edges[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (time + neighbor_time, neighbor))
        
        return total_time if len(visit) == n else -1