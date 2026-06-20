"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda a:a.start)

        if len(intervals) == 0:
            return True

        prevEnd = intervals[0].end

        for item in intervals[1:]:
            if item.start < prevEnd:
                return False
            prevEnd = item.end
        return True
