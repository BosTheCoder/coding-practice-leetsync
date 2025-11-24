class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in memo:
                return memo[(i,buying)]

            if buying:
                ret = max(
                    dfs(i+1, not buying) - prices[i],
                    dfs(i+1, buying)
                )
            else:
                ret = max(
                    dfs(i+2, not buying) + prices[i],
                    dfs(i+1, buying)
                )
            
            memo[(i,buying)] = ret
            return ret

        
        return dfs(0,True)
