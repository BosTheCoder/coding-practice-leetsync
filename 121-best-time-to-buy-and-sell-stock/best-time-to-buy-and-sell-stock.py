class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:    # len(prices) =6
            return 0
        left = 0   # 1
        right = 0   # 3
        maxp = 0    # 4
        while right < len(prices):
            if prices[left] > prices[right]:    # 7 > 7
                left = right

            total = -prices[left] + prices[right]   # 
            maxp = max(total,maxp)
            right += 1

        return maxp