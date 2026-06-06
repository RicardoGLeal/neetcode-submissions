import heapq

# The core challenge is that finding a median requires knowing the "middle" of all values
# seen so far — but inserting into a sorted structure costs O(n) and sorting from scratch
# each time costs O(n log n). The two-heap approach solves this by maintaining two halves
# of the data at all times: small (a max-heap) holds the lower half and large (a min-heap)
# holds the upper half. By keeping them balanced in size, the median is always sitting at
# one or both of their tops — making findMedian O(1). The only work happens during
# insertion, where we decide which half the new element belongs to and rebalance if needed,
# costing O(log n). This turns a naively expensive repeated-median problem into one that's
# efficient at every step.

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated) — stores the lower half
        self.large = []  # min-heap — stores the upper half

    def addNum(self, num: int) -> None:
        # push to the appropriate half based on value
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        # rebalance if either heap is more than 1 element ahead
        if len(self.small) - 1 > len(self.large):
            # move max of small to large
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)
        elif len(self.large) - 1 > len(self.small):
            # move min of large to small
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # odd total — small has the extra element, its max is the median
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            # odd total — large has the extra element, its min is the median
            return self.large[0]
        # even total — average the two middle elements
        return (-1 * self.small[0] + self.large[0]) / 2.0