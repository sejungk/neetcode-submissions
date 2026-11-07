"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda i: i.start)

        for i in range(1, n):
            prev = intervals[i - 1]
            curr = intervals[i]

            if prev.end > curr.start:
                return False
        return True