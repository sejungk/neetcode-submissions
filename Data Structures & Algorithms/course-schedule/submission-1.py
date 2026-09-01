class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_graph = {}
        
        for i in range(numCourses):
            adj_graph[i] = []
        
        for a, b in prerequisites:
            adj_graph[a].append(b)

        visited = set()
        def dfs(i):
            if i in visited:
                return False
            
            if len(adj_graph[i]) == 0:
                return True
            
            visited.add(i)
            for prereq in adj_graph[i]:
                if dfs(prereq) == False:
                    return False
            visited.remove(i)
            adj_graph[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True 