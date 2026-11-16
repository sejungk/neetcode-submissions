class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = [0] * n

        for a, b in trust:
            delta[a-1] -= 1
            delta[b-1] += 1
        
        for i in range(1, n + 1):
            if delta[i - 1] == n - 1:
                return i

        return -1

        