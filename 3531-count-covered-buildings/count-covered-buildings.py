class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xdict = defaultdict(list)
        xmax = defaultdict(lambda:-float("inf"))
        xmin = defaultdict(lambda:float("inf"))

        ydict = defaultdict(list)
        ymax = defaultdict(lambda:-float("inf"))
        ymin = defaultdict(lambda:float("inf"))

        for x, y in buildings:
            xdict[x].append(y)
            xmax[x] = max(y, xmax[x])
            xmin[x] = min(y, xmin[x])

            ydict[y].append(x)
            ymax[y] = max(x, ymax[y])
            ymin[y] = min(x, ymin[y])
        
        ret = 0
        for x,y in buildings:
            # check right
            if ymax[y] <= x:
                continue

            # check left
            if ymin[y] >= x:
                continue

            # check up
            if xmax[x] <= y:
                continue

            # check down
            if xmin[x] >= y:
                continue

            print(x,y)
            ret += 1
        
        return ret
"""

x -> y

1:2,1,3 (1,3)
2:4,3 (3,4)
3:1,2 (1,2)
4:3 (3,3)

y -> x

1:3,1 (1,3)
2:1,3 (1,3)
3:4,2,1 (1,4)
4:2 (2,2)

for 1,2 we check

to the right = (x,2) where x > 1
to the left = (x,2) where x < 1
upwards = (1,y) where y > 2
down = (1,y) where y < 2
"""