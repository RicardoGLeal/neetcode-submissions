class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # start with infinity so any price will replace it
        max_profit = 0            # worst case is no transaction, so profit is 0

        for price in prices:
            # update the cheapest buy price seen so far
            min_price = min(min_price, price)
            
            # if we sold today, this is the best profit we could make
            # (since we're using the lowest price seen before today)
            max_profit = max(max_profit, price - min_price)

        return max_profit