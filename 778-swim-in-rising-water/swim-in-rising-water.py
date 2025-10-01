import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # min-heap of (current_path_max, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False]*n for _ in range(n)]

        heappop = heapq.heappop
        heappush = heapq.heappush
        g = grid

        while heap:
            cur_max, i, j = heappop(heap)
            if visited[i][j]:
                continue
            visited[i][j] = True

            if i == n - 1 and j == n - 1:
                return cur_max

            # 4-neighbours
            if i+1 < n and not visited[i+1][j]:
                heappush(heap, (max(cur_max, g[i+1][j]), i+1, j))
            if i-1 >= 0 and not visited[i-1][j]:
                heappush(heap, (max(cur_max, g[i-1][j]), i-1, j))
            if j+1 < n and not visited[i][j+1]:
                heappush(heap, (max(cur_max, g[i][j+1]), i, j+1))
            if j-1 >= 0 and not visited[i][j-1]:
                heappush(heap, (max(cur_max, g[i][j-1]), i, j-1))
