class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr = float("inf")
        for price in prices:
            if price <curr:
                curr = price
            else:
                max_profit = max(price-curr, max_profit)
        return max_profit