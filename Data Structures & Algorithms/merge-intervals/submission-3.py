class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        res = [intervals[0]]
        n = len(intervals)

        for i in range(1, n):
            interval = intervals[i]
            if interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1] = [min(interval[0], res[-1][0]), max(interval[1], res[-1][1])]

        return res