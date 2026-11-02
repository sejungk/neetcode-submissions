class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for interval in intervals:
            if len(res) == 0 or interval[0] > res[-1][1]:
                res.append(interval)
            elif res[-1][1] >= interval[0]:
                res[-1] = [min(interval[0], res[-1][0]), max(interval[1], res[-1][1])]

        return res