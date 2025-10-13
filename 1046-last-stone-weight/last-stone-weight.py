class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            big, small = -heapq.heappop(heap), -heapq.heappop(heap)
            if big == small:
                continue

            diff = big-small
            heapq.heappush(heap,-diff)
        return -heap[0] if heap else 0

        