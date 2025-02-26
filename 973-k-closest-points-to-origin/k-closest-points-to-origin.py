class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(distances,(distance,[x,y]))
        
        ret = []
        while k:
            d, point = heapq.heappop(distances)
            ret.append(point)
            k-=1
        return ret
    
