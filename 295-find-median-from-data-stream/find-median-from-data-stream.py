class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-num)

        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            el = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, el)

        if len(self.minheap) - len(self.maxheap) > 1:
            el = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -el)
        elif len(self.maxheap) - len(self.minheap) > 1:
            el = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, el)
        

    def findMedian(self) -> float:
        total = len(self.minheap) + len(self.maxheap)
        if total % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            return -self.maxheap[0] if len(self.maxheap)> len(self.minheap) else self.minheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()