class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,buying):
            if (i,buying) in memo:
                return memo[(i,buying)]
            if buying is None:
                return 0
            if i>=len(prices):
                return 0
            
            skip = dfs(i+1,buying)

            if buying:
                v =  max(
                    skip,
                    dfs(i+1, not buying) - prices[i]
                )
            else:
                v = max(
                    skip,
                    dfs(i+1, None) + prices[i]
                )
            memo[(i,buying)] = v
            return v

        return dfs(0,True)