import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] 
        self.large = []
        
    def addNum(self, num: int) -> None:
        # small = maxHeap
        # large = minHeap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.small) - 1 > len(self.large):
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)
        elif len(self.large) - 1 > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0




        
        

