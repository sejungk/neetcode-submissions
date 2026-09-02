class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        remaining_prereqs = [0] * numCourses
        prereq_to_courses = {}

        for course in range(numCourses):
            prereq_to_courses[course] = []
        
        for course, prereq in prerequisites:
            prereq_to_courses[prereq].append(course)
            remaining_prereqs[course] += 1

        result = []
        def dfs(course):
            result.append(course)
            remaining_prereqs[course] -= 1

            for next_course in prereq_to_courses[course]:
                remaining_prereqs[next_course] -= 1
                if remaining_prereqs[next_course] == 0:
                    dfs(next_course)
            
        
       # Start with courses that have no prerequisites
        for course in range(numCourses):
            if remaining_prereqs[course] == 0:
                dfs(course)
        
        if len(result) != numCourses:
            return []

        return result