class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max heap
        distances = []

        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(distances,(-distance,[x,y]))
            if len(distances) > k:
                heapq.heappop(distances)

        return [d[1] for d in distances]
    

