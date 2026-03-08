class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for ix,point in enumerate(points):
            # print(point, (point[0]^2), (point[1]^2))
            distance = sqrt((point[0] ** 2) + (point[1]**2))

            if len(heap) <k:
                heapq.heappush(heap, (-distance,ix))
            else:
                # we're at capacity, something has to go if we want to add
                largest_dist_in_heap = -heap[0][0]
                if distance < largest_dist_in_heap:
                    heapq.heappush(heap,(-distance, ix))
                    heapq.heappop(heap)

        ret = []
        for dist, ix in heap:
            ret.append(points[ix])
        
        return ret
                