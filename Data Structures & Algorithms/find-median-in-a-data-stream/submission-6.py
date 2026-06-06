import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] 
        self.large = []
        
    def addNum(self, num: int) -> None:
        # small = maxHeap
        # large = minHeap
        if self.large and num > abs(self.large[0]):
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.small) - 1 > len(self.large):
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)
        elif len(self.large) - 1 > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)
        print("small: ", self.small)
        print("large: ", self.large)
        
    def findMedian(self) -> float:
        # midIdx = len(self.values) // 2
        size = len(self.large) + len(self.small)
        # print("size: "size)
        if size % 2 != 0:
            # odd
            return self.large[0] if len(self.large) > len(self.small) else -self.small[0]
        else:
            #even
            return (self.large[0] +(-self.small[0])) / 2




        
        

