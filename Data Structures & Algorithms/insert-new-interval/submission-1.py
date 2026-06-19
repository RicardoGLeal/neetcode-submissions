class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n, res = len(intervals), []
        i = 0

        # Phase 1: intervals that end before newInterval starts — settled, copy as-is
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Phase 2: intervals that overlap — fold each into newInterval, then append once
        # (phase 1 already guaranteed this interval ends >= newInterval's start,
        #  so checking only the start is enough to detect overlap)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]),
                           max(intervals[i][1], newInterval[1])]
            i += 1
        res.append(newInterval)  # unconditional: handles the no-overlap case for free

        # Phase 3: everything after newInterval — settled, copy as-is
        while i < n:
            res.append(intervals[i])
            i += 1

        return res