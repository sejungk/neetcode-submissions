class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        prereqs = defaultdict(set)
        for a, b in prerequisites:
            prereqs[b].add(a)

        visited = {}
        def dfs(a, b):
            if a in prereqs[b]:
                return True
            
            if (a, b) in visited:
                return visited[(a, b)]

            for nei in prereqs[b]:
                if dfs(a, nei):
                    visited[(a, b)] = True
                    return True

            visited[(a, b)] = False
            return False

        res = []
        for a, b in queries:
            res.append(dfs(a, b))

        return res
