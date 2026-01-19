class Solution:
    def mySqrt(self, x: int) -> int:
        r = x//2 +1
        l = 1

        while r>=l:
            m = l + (r-l)//2
            if m*m > x:
                r = m-1
            else:
                l = m + 1
        
        return r

"""
1 
2 l r m
3
4

"""