"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)

        for i in intervals:
            mp[i.start] += 1
            mp[i.end] -= 1

        rooms = 0
        res = 0

        for i in sorted(mp.keys()):
            rooms += mp[i]
            res = max(res, rooms)
        return res