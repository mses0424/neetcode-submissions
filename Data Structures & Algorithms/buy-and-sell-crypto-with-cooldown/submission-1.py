from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, can_buy: bool) -> int:
            if i >= n:
                return 0

            # 選擇 1：今天不動作（冷卻或繼續持有）
            cooldown_or_skip = dfs(i + 1, can_buy)

            if can_buy:
                # 選擇 2A：今天買入，明天變成不可買入狀態
                buy = dfs(i + 1, False) - prices[i]
                return max(cooldown_or_skip, buy)
            else:
                # 選擇 2B：今天賣出，因為有 1 天冷凍期，直接跳到 i + 2 天才能再買
                sell = dfs(i + 2, True) + prices[i]
                return max(cooldown_or_skip, sell)

        return dfs(0, True)