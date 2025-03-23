class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def getlargeststones():
            x = ix = y = iy = 0
            for i, stone in enumerate(stones):
                
                if stone > y:
                    # print("stone > y", stone, "i", i, "x",(x, ix), "y", (y,iy))
                    x = y
                    ix = iy
                    y = stone
                    iy = i
                elif stone > x:
                    # print("stone > x", stone, "i", i, "x",(x, ix), "y", (y,iy))
                    x = stone
                    ix = i
            return x, ix, y, iy
                
        # print(stones)
        while len(stones)>1:
            x, ix, y, iy = getlargeststones()
            if x == y:
                # print(f"deletion x {x} ix {ix} y {y} iy {iy}")
                del(stones[ix])
                del(stones[iy])
            else:
                # print(f"chipped x {x} ix {ix} y {y} iy {iy}")
                stones[iy] = y-x
                del(stones[ix])
            
            # print(stones)
                
        if not stones:
            return 0
        else:
            return stones[0]