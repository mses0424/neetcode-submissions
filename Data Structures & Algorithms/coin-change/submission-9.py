class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        total = [float('inf')] * (amount+1)
        total[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if i - c >= 0:
                    total[i] = min(total[i], total[i-c] + 1)
        return total[amount] if total[amount] != float('inf') else -1