class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            # get two heaviest stones
            big = -heapq.heappop(heap)
            small = -heapq.heappop(heap)
            
            # smash them togeher
            leftover= big-small

            # add back to heap if necessary
            if leftover:
                heapq.heappush(heap, -leftover)
        
        return -heap[0] if heap else 0