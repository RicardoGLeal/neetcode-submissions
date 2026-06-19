class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda a:a[0])
        prevEnd = intervals[0][1]

        for i,pair in enumerate(intervals):
            if i == 0:
                continue

            if pair[0] < prevEnd:
                res += 1
                prevEnd = min(prevEnd, pair[1])
            else:
                prevEnd = pair[1]
        return res 