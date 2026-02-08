class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_buy = 0
        prev_sell = 0
        prev_prev_buy = 0

        for i in range(len(prices)-1,-1,-1):
            curr_buy = max(prev_sell - prices[i], prev_buy)
            curr_sell = max(prev_sell, prev_prev_buy + prices[i])

            # shift everything back
            prev_prev_buy = prev_buy
            prev_buy = curr_buy
            prev_sell = curr_sell
        
        return curr_buy