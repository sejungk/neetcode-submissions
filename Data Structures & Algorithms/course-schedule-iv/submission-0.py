class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        prereqs = defaultdict(set)
        for a, b in prerequisites:
            prereqs[b].add(a)

        def dfs(a, b, visited):
            if a in prereqs[b]:
                return True
            
            if (a, b) in visited:
                return False
            
            visited.add((a, b))

            for nei in prereqs[b]:
                if dfs(a, nei, visited):
                    return True
            return False

        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res

