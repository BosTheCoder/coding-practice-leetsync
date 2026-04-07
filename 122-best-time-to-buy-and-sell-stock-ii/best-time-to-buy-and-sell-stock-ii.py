class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        buying = 0
        selling = 0

        for i in range(length-1, -1, -1):
            curr_price = prices[i]
            new_buying = max(-curr_price + selling, buying)
            new_selling = max(curr_price + buying, selling)
            buying = new_buying
            selling = new_selling
        
        return buying
"""
[1,4,2,6]


Buying = []
Selling = []
"""