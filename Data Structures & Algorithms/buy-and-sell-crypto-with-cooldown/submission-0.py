class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        prev_hold = -prices[0]
        prev_sell = 0
        prev_rest = 0
        for price in prices[1:]:
            hold = max(prev_hold,prev_rest - price)
            sell = prev_hold + price
            rest = max(prev_sell, prev_rest)
            prev_hold, prev_sell, prev_rest = hold, sell, rest
        return max(prev_sell,prev_rest)