class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def p(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            return time<=h
        
        max_k = max(piles)
        r = max_k + 1
        l = 1

        while r>l:
            mid = l+ (r-l)//2

            if p(mid):
                r=mid
            else:
                l=mid+1
        
        return l



"""
what p makes results space monotionic

p is whether can eat the banaas or not


def p(k):
    

"""