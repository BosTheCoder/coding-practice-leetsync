class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # memo = [None] * (len(cost)+1)

        # def dfs(i):
        #     if i>=len(cost):
        #         return 0
        #     if memo[i]:
        #         return memo[i]
        #     memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return memo[i]
        
        # return min(dfs(0), dfs(1))

        a, b = 0,0

        for i in range(len(cost)-1,-1,-1):
            temp = cost[i] + min(a, b)
            a, b = temp, a
        
        return min(a, b)