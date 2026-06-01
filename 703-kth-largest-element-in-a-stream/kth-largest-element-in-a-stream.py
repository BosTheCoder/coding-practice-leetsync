class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


"""

top of the heap = kth largest

bottom of the heap = largest

so it's go to be a min heap

how do we keep small values out?

5
    6
    7
        9

we only add values when it's larger than the top
if it's not we skip it
if it is we add then 


easier method is just to add everytime
then if it's greater than k just pop

the add method always returns the value after all operations done

"""