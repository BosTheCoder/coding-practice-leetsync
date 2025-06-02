class MedianFinder:

    def __init__(self):
        self.sorted_list = []

    def addNum(self, num: int) -> None:
        bisect.insort_right(self.sorted_list, num)

    def findMedian(self) -> float:
        length = len(self.sorted_list)
        half = length/2
        if length%2 == 0:
            a = int(half)
            b = a - 1
            return (self.sorted_list[a] + self.sorted_list[b]) /2
        else:
            a = int(half)
            return self.sorted_list[a]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()