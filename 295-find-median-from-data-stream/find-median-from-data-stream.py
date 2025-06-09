class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            max_element = -(heapq.heappop(self.maxheap))
            heapq.heappush(self.minheap, max_element)

        if len(self.maxheap) > len(self.minheap) + 1:
            max_element = -(heapq.heappop(self.maxheap))
            heapq.heappush(self.minheap, max_element)
        elif len(self.minheap) > len(self.maxheap) + 1:
            min_element = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -min_element)

            

    def findMedian(self) -> float:
        total_length = len(self.maxheap) + len(self.minheap)
        if total_length % 2 == 0:
            median = (-self.maxheap[0] + self.minheap[0])/2
        else:
            median = -(self.maxheap[0]) if len(self.maxheap) > len(self.minheap) else self.minheap[0]     

        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()