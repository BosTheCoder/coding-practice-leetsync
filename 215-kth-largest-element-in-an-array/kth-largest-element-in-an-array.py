class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap, num)
            else:
                if num<=heap[0]:
                    pass
                else:
                    heapq.heappush(heap, num)
                    heapq.heappop(heap)
        
        return heap[0]