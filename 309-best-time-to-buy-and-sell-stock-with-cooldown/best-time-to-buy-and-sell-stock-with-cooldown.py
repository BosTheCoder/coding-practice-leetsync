class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (i, buying)

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]
            
            cool = dfs(i+1, buying)

            if buying:
                buy = -prices[i] + dfs(i+1, False)
                dp[(i,buying)] = max(buy, cool)
            else:
                sell = prices[i] + dfs(i+2, True)
                dp[(i,buying)] = max(sell, cool)
            
            return dp[(i,buying)]
        
        return dfs(0,True)

