class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()

        res = 0
        for i in range(1, n):
            prev = intervals[i - 1]
            curr = intervals[i]

            if prev[1] > curr[0]:
                curr[1] = min(curr[1], prev[1])
                res += 1
        
        return res
