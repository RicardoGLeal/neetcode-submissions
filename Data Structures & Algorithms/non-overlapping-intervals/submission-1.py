class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Min intervals to remove so none overlap = greedy (activity selection).
        # Sort by start, sweep left to right. On overlap, keep the one ending
        # EARLIER (min end) — it blocks less ahead, causing fewer future conflicts.
        # O(n log n) time, O(1) space.

        res = 0  # count of intervals we must remove

        # Sort by start time so we process intervals left to right.
        intervals.sort(key=lambda a: a[0])

        # Track the end of the interval we're currently "keeping."
        prevEnd = intervals[0][1]

        # Compare each following interval against the one we kept.
        for start, end in intervals[1:]:
            if start < prevEnd:
                # Overlap: drop one, keep whichever ends sooner.
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                # No overlap: keep it and advance prevEnd.
                prevEnd = end

        return res