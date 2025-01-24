class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        WALL = -1
        GATE = 0

        def dfs(i, j, depth) -> None:
            tab = " " * depth
            # print(f"{tab}dfs {i},{j},{depth}")
            if i >= len(rooms) or i<0 or j >= len(rooms[0]) or j <0:
                return

            cell = rooms[i][j]

            if cell == WALL or cell == GATE or (depth>=cell):
                # print(f"{tab}returning", cell, depth)
                return
            
            # print(f"{tab}setting value {i},{j} to {depth}")
            rooms[i][j] = depth

            depth += 1
            dfs(i + 1, j, depth)
            dfs(i, j + 1, depth)
            dfs(i, j-1, depth)
            dfs(i-1,j, depth)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                cell = rooms[i][j]
                if cell == GATE:
                    dfs(i + 1, j, 1)
                    dfs(i, j + 1, 1)
                    dfs(i, j-1, 1)
                    dfs(i-1,j, 1)
