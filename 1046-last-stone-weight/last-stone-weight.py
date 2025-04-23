class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        #need to make all stone weights negative to make it a min heap
        for stone in stones:
            heapq.heappush(heap,-stone)
        
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 == stone2:
                continue
            new_stone = abs(stone1-stone2)
            heapq.heappush(heap, -new_stone)
        
        return -heap[0] if heap else 0