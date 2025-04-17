class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if i see a 1 add index to seen array straight away
        # go to all nodes nearby that have a q
        # if i see a node thats not in seen, +1 to counter
        # if node is seen go back and add nothing to counter

        seen = set()
        maxs = 0
        directions = [
            [0,1],
            [1,0],
            [-1,0],
            [0,-1]
        ]
        def dfs(i,j,size):
            nonlocal maxs
            seen.add((i,j))
            maxs = max(maxs,size)
            for dir in directions:
                c =(i+dir[0],j+dir[1])
                if c[0]>=len(grid) or c[0]<0 or c[1]>=len(grid[0]) or c[1]<0:
                    continue
                if not grid[c[0]][c[1]] or c in seen:
                    continue
                size = max(size,dfs(c[0], c[1], size+1))
            return size 

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in seen:
                    dfs(i,j,1)
        return maxs

