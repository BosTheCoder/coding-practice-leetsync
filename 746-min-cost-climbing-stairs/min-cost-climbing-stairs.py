class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        prevprev = 0

        for i in range(len(cost)-1,-1,-1):
            curr = min(cost[i]+prev, cost[i]+prevprev)
            prevprev = prev
            prev = curr
        
        return min(prev, prevprev)
