class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i, [a, b] in enumerate(edges):
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))

        min_heap = []
        heapq.heappush(min_heap, (-1, start_node))
        visited = set()
        while min_heap:
            prob, node = heapq.heappop(min_heap)

            if node == end_node:
                return prob * -1

            if node in visited:
                continue

            visited.add(node)

            for nei, nei_prob in adj[node]:
                heapq.heappush(min_heap, (nei_prob * prob, nei))
            
        return 0

