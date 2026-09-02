class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        indegree = [0] * numCourses
        prereq_to_course = {}

        for i in range(numCourses):
            prereq_to_course[i] = []
        
        for a, b in prerequisites:
            prereq_to_course[b].append(a)
            indegree[a] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        visited = set()
        while queue:
            course = queue.popleft()
            result.append(course)
            for course in prereq_to_course[course]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        if len(result) != numCourses:
            return []

        return result
                

