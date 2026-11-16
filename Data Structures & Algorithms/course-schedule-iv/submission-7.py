class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        prereqs = defaultdict(set)
        for a, b in prerequisites:
            prereqs[b].add(a) # course: prerequisties

        def dfs(i, pre):
            if i in pre:
                return
            
            pre.add(i)

            for j in prereqs[i]:
                dfs(j, pre)
            
            
        for i in range(numCourses):
            course = set()
            dfs(i, course)
            
            for a in course:
                prereqs[i].add(a)

        res = []
        for a, b in queries:
            res.append(a in prereqs[b])

        return res
