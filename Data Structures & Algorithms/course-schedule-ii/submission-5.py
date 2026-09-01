class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_prereq = {}
        for i in range(numCourses):
            course_to_prereq[i] = []
        
        for a, b in prerequisites:
            course_to_prereq[a].append(b)

        visited = set()
        visited_in_path = set()
        result = []
        def dfs(course):
            if course in visited_in_path:
                return False

            if course in visited:
                return True
            
            visited_in_path.add(course)
            for pre in course_to_prereq[course]:
                if dfs(pre) == False:
                    return False
            
            visited_in_path.remove(course)
            visited.add(course)
            result.append(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
            
        return result
