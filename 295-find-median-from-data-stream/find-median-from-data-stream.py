class MedianFinder:

    def __init__(self):
        self.maxh = [] # left
        self.minh = [] # right
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -num)

        # check values
        if self.minh and -self.maxh[0] > self.minh[0]:
            val = -heapq.heappop(self.maxh)
            heapq.heappush(self.minh, val)
        
        # reorganize lists:
        if len(self.maxh) > len(self.minh) + 1:
            val = -heapq.heappop(self.maxh)
            heapq.heappush(self.minh, val)
        elif len(self.minh) > len(self.maxh) + 1:
            val = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -val)


    def findMedian(self) -> float:
        if len(self.maxh) == len(self.minh):
            return (-self.maxh[0] + self.minh[0]) /2
        elif len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        else:
            return self.minh[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()