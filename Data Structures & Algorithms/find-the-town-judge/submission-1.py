class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdegrees = [0] * n
        indegrees = [0] * n

        for a, b in trust:
            outdegrees[a-1] += 1
            indegrees[b-1] += 1
        
        for i in range(1, n + 1):
            if outdegrees[i - 1] == 0 and indegrees[i - 1] == n - 1:
                return i

        return -1

        