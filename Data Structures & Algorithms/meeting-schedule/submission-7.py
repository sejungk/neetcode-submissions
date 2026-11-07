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
        if n == 0:
            return True

        max_val = max(interval.end for interval in intervals)

        ends = [-1] * (max_val + 1)
        for interval in intervals:
            if ends[interval.start] != -1:
                return False

            ends[interval.start] = interval.end

        end = -1
        for i in range(max_val + 1):
            if i == end:
                end = -1
                
            if ends[i] != -1:
                if end != -1:
                    return False
                else:
                    end = ends[i]

            

        return True