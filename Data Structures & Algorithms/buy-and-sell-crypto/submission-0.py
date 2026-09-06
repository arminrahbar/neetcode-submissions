class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        max_profit = 0

        for price in prices[1:]:

            profit = price - lowest

            if profit > max_profit:
                max_profit = profit
    
            if price < lowest:
                lowest = price

        return max_profit

