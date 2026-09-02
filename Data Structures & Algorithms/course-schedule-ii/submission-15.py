class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        course_to_prereq = {}

        for i in range(numCourses):
            course_to_prereq[i] = []
        
        for a, b in prerequisites:
            course_to_prereq[a].append(b)

        result = []

        def dfs(course):
            if course in visited:
                return True
            
            if course in cycle:
                return False
            
            cycle.add(course)
            for prereq in course_to_prereq[course]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return result