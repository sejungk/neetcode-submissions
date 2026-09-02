class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)] 

        for a, b in prerequisites:
            indegree[b] += 1
            adj[a].append(b)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        visited = set()
        while queue:
            course = queue.popleft()
            result.append(course)
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != numCourses:
            return []

        return result[::-1]
                

