class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        # pop them bad boys
        while len(heap) >= 2:
            # pop 2
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)

            if a == b:
                # do nothing as they're both destroyde
                continue
            
            heapq.heappush(heap, -(a-b))
        
        return -heap[0] if heap else 0
