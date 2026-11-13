class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total = [0] * (amount+1)
        total[0] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                total[i] += total[i-coin]
        print(total)
        return total[amount]