class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid(k):
            if k ==0:
                return k 
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            return total <= h
            

        l = 0
        r = max(piles)
        while l < r:
            mid = l + (r-l)//2
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        
        return r