class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for day in range(1,len(prices)):
            if prices[day] - prices[day-1] > 0:
                total += prices[day] - prices[day-1]
        return total