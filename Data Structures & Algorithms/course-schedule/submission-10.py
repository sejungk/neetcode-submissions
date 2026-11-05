class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        indegree = {}
        
        for i in range(numCourses):
            adj[i] = []
            indegree[i] = 0

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count == numCourses