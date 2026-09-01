class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_graph = {}
        
        for i in range(numCourses):
            adj_graph[i] = []
        
        for a, b in prerequisites:
            adj_graph[a].append(b)

        visited = set()
        def dfs(i, courses_in_this_path):
            if i in visited:
                return True

            if i in courses_in_this_path:
                return False
            
            if len(adj_graph[i]) == 0:
                return True
            
            courses_in_this_path.add(i)
            for prereq in adj_graph[i]:
                if dfs(prereq, courses_in_this_path) == False:
                    return False
            visited.add(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True 