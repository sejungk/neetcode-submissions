"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res = 0
        count = 0
        s = 0
        e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            elif start[s] >= end[e]:
                e += 1
                count -= 1
            
            res = max(res, count)
        return res