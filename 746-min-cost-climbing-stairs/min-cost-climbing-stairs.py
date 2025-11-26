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

        memo = [0] * (len(cost)+2)

        for i in range(len(cost)-1,-1,-1):
            memo[i] = cost[i] + min(memo[i+1], memo[i+2])
        
        return min(memo[0], memo[1])