class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_prereq = {}
        prereq_to_course = {}
        queue = deque()

        for i in range(numCourses):
            course_to_prereq[i] = []
            prereq_to_course[i] = []

        for a, b in prerequisites:
            course_to_prereq[a].append(b)
            prereq_to_course[b].append(a)

        for course in course_to_prereq:
            if len(course_to_prereq[course]) == 0:
                queue.append(course)
        
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            
            for post_req in prereq_to_course[course]:
                course_to_prereq[post_req].remove(course)

                # All prerequisites are now satisfied
                if len(course_to_prereq[post_req]) == 0:
                    queue.append(post_req)

        if len(result) < numCourses:
            return []
        return result