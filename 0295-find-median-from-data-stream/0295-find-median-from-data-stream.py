class MedianFinder:

    def __init__(self):
        self.maxheap, self.minheap = [], [] # stores the lower half, upper half

    def addNum(self, num: int) -> None:
        # first push to the maxheap
        if len(self.maxheap)==len(self.minheap):
            if self.minheap and num>self.minheap[0]:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        else:
            # check if the maxheap element needs to be shifted to minheap
            if -self.maxheap[0]>num:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)

    def findMedian(self) -> float:
        if len(self.maxheap)==len(self.minheap):
            return (self.minheap[0]-self.maxheap[0])/2
        return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()