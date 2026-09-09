class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_graph = [[] for _ in range(n + 1)]

        for u,v,t in times:
            adj_graph[u].append((v, t))
        
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, curr_time):
            if curr_time >= dist[node]:
                return

            dist[node] = curr_time

            for neighbor, time in adj_graph[node]:
                dfs(neighbor, curr_time + time)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1    