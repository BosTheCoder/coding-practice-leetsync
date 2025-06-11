class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        have a min heap which stores (time at this point, (x,y))
        you have a while loop that 
        1. pops from the min heap t and x,y
        1.1 check if (X,y) is in seen hash table, if it is then skip
        1.2. if it isn't then add it in there
        2. if x,y is (n-1,n-1) end algo and return t
        3. if not continue
        4. adds all 4 adjacent squares to the heap with their correct times
        

        """

        heap = []
        n = len(grid)
        seen = set()
        coords= [(0,1),(1,0), (-1,0), (0,-1)]
        heapq.heappush(heap, (grid[0][0], 0, 0))
        while heap:
            t, x , y = heapq.heappop(heap)
            if x == n-1 and y == n-1:
                return t
            
            if (x,y) in seen:
                continue
            else:
                seen.add((x,y))
            
            for ax, ay in coords:
                nx = x + ax
                ny = y + ay

                if nx >= n or nx < 0 or ny >= n or ny < 0 or (nx,ny) in seen:
                    continue
                
                newt = grid[ny][nx]
                heapq.heappush(heap, ((max(t, newt)), nx, ny))
        
        return False