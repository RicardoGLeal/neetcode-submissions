"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
            
        intervals.sort(key=lambda a: a.start)

        # 1. create heap. add end time of first interval
        heap = []
        heapq.heappush(heap, intervals[0].end)

        # 2. sweep through intervals. Validate if current interval can be accomodated in the earliest meeting to end
        for interval in intervals[1:]:
            if interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)
