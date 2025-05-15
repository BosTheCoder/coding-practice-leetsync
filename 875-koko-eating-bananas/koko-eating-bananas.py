class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def caneat(k) -> bool:
            hours =0
            for pile in piles:
                hours += pile//k +1 if pile%k !=0 else pile//k
            return hours <= h
        
        left, right = 1, max(piles)+1

        while right - left > 1:
            mid = (right + left) // 2
            cn = caneat(mid)
            # print(mid, cn)
            if not cn:
                left = mid
            else:
                right = mid
            # print("left", left, "right", right)
        
        return left if caneat(left) else right
            

"""
k < max(largest pile)

can do binary search between 0 & k?

to figure out if a value k can do the job you can go through each value in the array

val // k + 1 if val%k !=0 else val//k

time complexity

each time in binary search need to do p operations
binary search is plogp so maybe plogp^2
"""