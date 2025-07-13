class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memoization arrays
        b = [0,0]
        s = 0

        for i in range(len(prices)-1,-1,-1):
            price = prices[i]
            
            b_new = max(s - price,b[0])
            s_new = max(b[1] +price, s)

            b = [b_new, b[0]]
            s = s_new
        return b[0]