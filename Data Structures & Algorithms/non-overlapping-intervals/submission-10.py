class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()

        prev = intervals[0][1]
        res = 0
        for i in range(1, n):
            curr = intervals[i]

            if prev > curr[0]:
                prev = min(curr[1], prev)
                res += 1
            else:
                prev = curr[1]
        return res
