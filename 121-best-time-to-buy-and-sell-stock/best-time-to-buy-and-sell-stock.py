class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        start, end = 0,0
        maxp = 0
        while end< len(prices):
            p = prices[end] - prices[start]
            if p<0:
                start = end
            else:
                maxp = max(p,maxp)
                end += 1
            
            
        return maxp
            