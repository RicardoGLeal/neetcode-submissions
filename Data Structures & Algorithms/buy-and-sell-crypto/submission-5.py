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


    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1      # l = buy day, r = sell day, start adjacent
        maxP = 0         # worst case is no transaction, so profit is 0

        while r < len(prices):
            if prices[l] < prices[r]:
                # selling at r is profitable, compute and track it
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # prices[r] is cheaper than prices[l], so it's a better
                # buy day — no point holding onto the old buy price
                l = r
            
            # always advance the sell pointer to explore future days
            r += 1

        return maxP