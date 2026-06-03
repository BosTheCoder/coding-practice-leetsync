class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # creating max heap
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        

        # processing heap
        while len(heap)>1:
            val_a = -heapq.heappop(heap)
            val_b = -heapq.heappop(heap)

            remainder = val_a - val_b

            if remainder>0:
                heapq.heappush(heap, -remainder)
        
        return -heap[0] if heap else 0
