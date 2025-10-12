class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        l=r=0
        while r< len(prices):
            mp=max(mp, prices[r]-prices[l])
            if prices[l]>prices[r]:
                l=r
            r+=1
        return mp