class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        height = width = len(grid)
        heapq.heappush(heap, (grid[0][0],0,0)) # time, i, j
        seen = set()
        seen.add((0,0))

        count = 0
        while heap:
            count += 1
            t, i, j = heapq.heappop(heap)
            
            if (i,j) == (width-1, height-1):
                return t
            
            for di, dj in dirs:
                ni,nj = i+di, j+dj

                if ni>=width or ni<0 or nj>=height or nj <0 or (ni,nj) in seen:
                    continue
                
                val = (max(t, grid[nj][ni]), ni, nj)

                if (ni,nj) == (width-1,height-1):
                    return val[0]
                seen.add((ni,nj))
                heapq.heappush(
                    heap, 
                    val
                )
        return None
            
