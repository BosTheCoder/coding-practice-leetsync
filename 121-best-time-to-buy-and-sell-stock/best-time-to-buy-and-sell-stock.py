class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Using the intuitive method

        max_prof = 0

        lowest_price = float("inf")
        for curr_price in prices:
            lowest_price = min(lowest_price,curr_price)
            curr_prof = curr_price - lowest_price
            max_prof = max(curr_prof, max_prof)
        
        return max_prof
