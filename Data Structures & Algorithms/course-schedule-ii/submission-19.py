class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {}

        for i in range(numCourses):
            prereqs[i] = []

        for a, b in prerequisites:
            prereqs[a].append(b)

        res = []
        cycle = set()
        visited = set()
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for pre in prereqs[crs]:
                if dfs(pre) == False:
                    return False
                
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
            
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res