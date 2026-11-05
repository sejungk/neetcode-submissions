class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for a, b in prerequisites:
            adj[b].append(a)

        visited = set()
        visiting = set()
        def cycle(node):
            if node in visited:
                return False
            
            if node in visiting:
                return True
            
            visiting.add(node)
            for nei in adj[node]:
                if cycle(nei):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False    

        for i in range(numCourses):
            if cycle(i):
                return False
        
        return True