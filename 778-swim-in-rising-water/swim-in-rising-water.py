class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0],0,0)]
        heapq.heapify(heap)
        seen = set()
        coords = [(0,1),(1,0),(-1,0),(0,-1)]

        while heap:
            maximum, i, j = heapq.heappop(heap)
            
            if (i,j) in seen:
                continue            

            # Add to seen
            seen.add((i,j))

            if (i,j) == (n-1,n-1):
                return maximum
            
            for coord in coords:
                ni = coord[1] + i
                nj = coord[0] + j

                if (
                    ni <0 or ni>=n or
                    nj <0 or nj>=n
                ):
                    continue

                new_maximum = max(maximum, grid[nj][ni])
                heapq.heappush(heap,(new_maximum,ni,nj))
            
        return False

        


    # def swimInWater(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     seen = [[0] * n for i in range(n)]
    #     coords = [(0,1),(1,0),(-1,0),(0,-1)]

    #     def dfs(i, j, curr_max):          
    #         if i == n-1 and j == n-1:
    #             return curr_max
            
    #         curr_max = max(
    #             grid[j][i],
    #             curr_max
    #         )

    #         min_val = float("inf")
    #         for coord in coords:
    #             ni = coord[0] + i
    #             nj = coord[1] + j

    #             if (
    #                 ni <0 or ni>=n or
    #                 nj <0 or nj>=n
    #             ):
    #                 continue
                
    #             min_val = min(
    #                 min_val,
    #                 dfs(ni,ni,curr_max)
    #             )
            
    #         return min_val
        
    #     return dfs(0,0,0)


