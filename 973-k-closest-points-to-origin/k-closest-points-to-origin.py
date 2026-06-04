class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point: list[int]) -> int:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            return dist
        

        heap = []
        for point in points:
            heapq.heappush(heap, (-distance(point), point[0], point[1]))
            if len(heap) > k:
                heapq.heappop(heap)
            
        
        return [[x,y] for dist,x,y in heap]