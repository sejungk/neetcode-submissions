class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_prereq = {}
        for i in range(numCourses):
            course_to_prereq[i] = []
        
        for a, b in prerequisites:
            course_to_prereq[a].append(b)

        visited = set()
        result = []
        def dfs(course, visiting_in_path):
            if course in visiting_in_path:
                return False

            if course in visited:
                return True
            
            visiting_in_path.add(course)
            for pre in course_to_prereq[course]:
                if dfs(pre, visiting_in_path) == False:
                    return False
            
            visiting_in_path.remove(course)
            visited.add(course)
            result.append(course)

            return True

        for course in range(numCourses):
            if dfs(course, set()) == False:
                return []
            
        return result
